# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. **Endpoint (`app.py`)**: A `POST /submit` request arrives at Provenance Guard, a web service, which receives the text, validates it, and assigns a `content_id`.
2. **Predictability signal (`detector.py`)**: Runs GPT-2, a language model, to measure how predictable the text is, with a 0–1 score. Higher means more AI-like.
3. **Style signal (`stylometry.py`)**: Measures features such as sentence-length variation, vocabulary variety, and punctuation, without interpreting the text's meaning. It returns a second 0–1 score.
4. **Combining (`scoring.py::combine_signals`)**: Merges the two scores into a single 0–1 `confidence` score.
5. **Labeling (`scoring.py::score_to_label`)**: Turns `confidence` into one of three labels, `human`, `unsure`, or `ai`, plus a plain-language sentence written for the writer.
6. **Logging and response (`audit.py`, `app.py`)**: The decision is logged as a JSON line, then returned to the writer with both signal scores, the `confidence`, and the label.
7. **Appeal (`app.py`, `audit.py`)**: If the writer disagrees, they can later send `POST /appeal` with the `content_id` and their reasoning. The service checks the ID exists, records the challenge, and places the item under review.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to a language model (gpt2, run locally). `detector.py::model_signal` computes the perplexity and squashes it onto 0–1 with a logistic curve, where higher means more likely AI. A perplexity of 45 scores 0.5.

**Why that might differ between human and AI writing:** A language model writes by picking likely next words, so text it produced tends to be text another model finds easy to predict. Human writing wanders more, with odd word choices and specific details.

**What it can't see:** Authorship. It rewards common words in short, ordinary sentences, and plenty of people write that way. On my calibration inputs it did exactly this. My own plainly written bio scored 0.844, higher than the AI-written tea paragraph at 0.763. The edited AI text scored the lowest of all (0.655) because its names, dates and places raised the perplexity. Plain human writing is the case this signal is most likely to get wrong.

### Signal two — the style signal

**What it measures:** The shape of the text, without reading it. `stylometry.py::style_signal` combines three measures: sentence length spread (the coefficient of variation of sentence lengths), type-token ratio (unique words over total words) and punctuation density (marks per word). Each is flipped where needed and scaled to 0–1, then they are averaged with weights of 0.4, 0.35 and 0.25. Higher means more likely AI.

**Why that might differ between human and AI writing:** Generated prose tends toward even, mid-length sentences and a narrower vocabulary. Human writing is lumpier, with short sentences next to long ones.

**What it can't see:** What the text says. Anything that changes the shape without changing the substance moves it, such as adding typos, splitting sentences or pasting in a quotation. It also barely separated my four calibration inputs, scoring 0.51–0.58 on all of them, so on its own it has no strong opinion. The punctuation direction is untested.

### The combining rule

**The rule:** Both signals point the same way (higher means more likely AI). The service takes a weighted average that favours the model signal, because the style signal stays close to 0.5 and would otherwise pull every score into the middle. When the two signals disagree by a large margin, neither is trusted and the result is set to 0.5, which is unsure.

**The numbers:**

| Setting | Value | Where |
|---|---|---|
| Model-signal weight | 0.70 | `config.WEIGHT_MODEL_SIGNAL` |
| Style-signal weight | 0.30 | `config.WEIGHT_STYLE_SIGNAL` |
| Disagreement gap | signals differ by more than 0.50 | `config.DISAGREEMENT_GAP` |
| Score on disagreement | 0.50 | `config.DISAGREEMENT_SCORE` |
| High-confidence human | 0.22 or below | `config.HUMAN_THRESHOLD` |
| Unsure | above 0.22 and below 0.78 | |
| High-confidence AI | 0.78 or above | `config.AI_THRESHOLD` |

I first planned 0.5/0.5 with a 0.4 gap, but a model score of 0.95 against a style score of 0.5 was forced to unsure. So I moved to 0.7/0.3 and a 0.5 gap. With a style score near 0.5, the AI label now needs a model score of roughly 0.9 or more, and the human label roughly 0.1 or less.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

My four calibration inputs, run through both signals and the combining rule:

The Label column is what the thresholds imply. `/submit` still returns a placeholder label until Milestone 5.

| Piece | Perplexity | Model | Style | Combined | Label |
|---|---|---|---|---|---|
| clearly_ai (tea) | 21.7 | 0.763 | 0.507 | 0.686 | unsure |
| clearly_human (my bio) | 15.7 | 0.844 | 0.551 | 0.756 | unsure |
| formal_human (meditation) | 20.3 | 0.782 | 0.578 | 0.721 | unsure |
| edited_ai (Wright brothers) | 30.1 | 0.655 | 0.559 | 0.626 | unsure |

The biggest split is my own bio. The model signal reads it as AI (0.844) while the style signal sits in the middle (0.551), a gap of 0.29. That is below the 0.50 disagreement gap, so the rule does not step in. It averages the two and gets 0.756, which falls in unsure, just under the 0.78 AI threshold. The averaging and the wide unsure band are what stop my own writing being called AI.

What this run also showed:

- **The signals did not separate human from AI.** The combined scores rank my bio highest, then meditation, tea and the edited AI text, the reverse of what I expected. Changing the weights or the gap would move all four pieces together, so it would not fix this. I did not retune the model signal's midpoint either, because four texts is too few to tune on.
- **The disagreement rule never triggered.** The signals differed by only 0.1–0.3 on every input, because the style signal barely moves.
- **Every input landed in unsure.** That is the safe way to fail, since nobody is wrongly accused, but the service says little on these inputs.
- **My bio is close to the AI threshold.** A slightly more predictable human text would be labelled AI. This is the false positive I am most worried about, and the 0.78 threshold is the main protection against it.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human |  |  |
| unsure |  |  |
| high-confidence AI |  |  |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "...", "creator_id": "..."}'
```

```json

```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json

```

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
