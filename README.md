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

**What it can't see:** Authorship. It rewards common words in short, ordinary sentences, and plenty of people write that way. On my calibration inputs it did exactly this. My own plainly written bio scored 0.844, higher than the AI-written tea paragraph at 0.763. The edited AI text scored the lowest of all (0.655) probably because its names, dates and places raised the perplexity, though I did not test that. Plain human writing is the case this signal is most likely to get wrong.

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

| Piece | Perplexity | Model | Style | Combined | Label |
|---|---|---|---|---|---|
| clearly_ai (tea) | 21.7 | 0.763 | 0.507 | 0.686 | unsure |
| clearly_human (my bio) | 15.7 | 0.844 | 0.551 | 0.756 | unsure |
| formal_human (meditation) | 20.3 | 0.782 | 0.578 | 0.721 | unsure |
| edited_ai (Wright brothers) | 30.1 | 0.655 | 0.559 | 0.626 | unsure |

The biggest split is my own bio. The model signal reads it as AI (0.844) while the style signal sits in the middle (0.551), a gap of 0.29. That is below the 0.50 disagreement gap, so the rule does not step in. It averages the two and gets 0.756, which falls in unsure, just under the 0.78 AI threshold. The averaging and the wide unsure band are what stop my own writing being called AI.

A made-up pair, model 0.9 and style 0.1, has a gap of 0.8, so `combine_signals` returns 0.5 (unsure) instead of the 0.66 average. I confirmed this by calling it directly.

What this run also showed:

- **The signals did not separate human from AI.** The combined scores rank my bio highest, then meditation, tea and the edited AI text, the reverse of what I expected. Changing the weights or the gap would move all four pieces together, so it would not fix this. I did not retune the model signal's midpoint either, because four texts is too few to tune on.
- **Every input landed in unsure.** That is the safe way to fail, since nobody is wrongly accused, but the service says little on these inputs.
- **My bio is close to the AI threshold.** A slightly more predictable human text would be labelled AI. This is the false positive I am most worried about, and the 0.78 threshold is the main protection against it.



---

## Label Variants

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.22 or below | "We think this was probably written by a person." |
| unsure | above 0.22 and below 0.78 | "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way." |
| high-confidence AI | 0.78 or above | "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong." |

**Why I worded the "unsure" one this way:**
Most of my calibration inputs, including my own bio, landed in this band, so it's the label writers will see most. It says plainly that we're not sure, tells the writer no action is needed, and names plain writing as a known trigger so it doesn't read as an accusation. It avoids numbers and words like "threshold" or "flagged".



---

## Sample Run

I submitted my formal_human piece (the meditation essay I wrote myself). It scored 0.721, just under the 0.78 AI threshold, so it was labelled unsure. I appealed it anyway to show the appeal path.

**A submission**

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "The subject of meditation presents interesting ideas regarding achieving happiness. It may not be suitable or easy for everyone, but studies show that people who meditate regularly have improved their physical, mental, and emotional well-being. All you need to meditate is a quiet place to sit, clear your mind, and focus on your breathing. However, just as the world possesses a multitude of cultures, meditation has branched into many different forms. Despite its variations, perhaps the hardest part is accepting the undeniable truth that pain is inevitable. Only by finding pleasure within pain can we find peace and contentment. It may not be the happiness we expected, but know that it is a happiness we can achieve.", "creator_id": "formal_human"}'
```

```json
{
  "confidence": 0.7207253832352577,
  "content_id": "f8268153-7fc6-4fef-a7ef-30b9683805af",
  "guess": "unsure",
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "model_score": 0.7819,
  "style_score": 0.5779846107841924
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "f8268153-7fc6-4fef-a7ef-30b9683805af", "reasoning": "I wrote this passage on meditation myself. Its formal, reflective tone likely triggered the AI label. I can share my drafts on request and ask for a human review."}'
```

```json
{
  "content_id": "f8268153-7fc6-4fef-a7ef-30b9683805af",
  "message": "Your appeal has been recorded and the decision is now under review.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.7207253832352577,
      "content_id": "f8268153-7fc6-4fef-a7ef-30b9683805af",
      "creator_id": "formal_human",
      "guess": "unsure",
      "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
      "model_score": 0.7819,
      "status": "decided",
      "style_score": 0.5779846107841924,
      "timestamp": "2026-11-04T05:19:45+00:00"
    },
    {
      "content_id": "f8268153-7fc6-4fef-a7ef-30b9683805af",
      "creator_id": "formal_human",
      "event": "appeal",
      "reasoning": "I wrote this passage on meditation myself. Its formal, reflective tone likely triggered the AI label. I can share my drafts on request and ask for a human review.",
      "status": "under_review",
      "timestamp": "2026-11-04T05:19:45+00:00"
    }
  ]
}
```

The original decision stays in the log with status `decided`, and the appeal is added after it with status `under_review`. Nothing is overwritten.

---

## How I Used AI

**Moment 1**

- *What I asked for:* Whether an equal-weight average with 0.22/0.78 thresholds, where disagreement pulls toward unsure, would work as my combining rule.
- *What came back:* The idea was sound, but my style signal stayed near 0.5, so the human and AI labels were almost unreachable. It suggested 0.7/0.3 weights and an explicit rule that sets the score to 0.5 when the signals differ by more than a gap.
- *What I changed:* I kept my own 0.22/0.78 thresholds. The first gap (0.4) blocked confident AI results in testing, so it became 0.5. I recorded my calibration results in the README rather than tuning the numbers to fit them.

**Moment 2**

- *What I asked for:* What was wrong with my `curl.exe` command for `/appeal`, which I ran in PowerShell with the JSON body in single quotes.
- *What came back:* PowerShell strips the inner double quotes before `curl.exe` sees them, so the server got invalid JSON. My route turned that into an empty object, which is why the error said `content_id is required` instead of `invalid_json`. It suggested a here-string piped to curl, `Invoke-RestMethod`, or escaping every quote.
- *What I changed:* I put the JSON in a here-string and piped it to `curl.exe` with `--data-binary "@-"`. The appeal then went through and showed up in the log.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 5 per minute, 50 per day

**Why those numbers and not others:** A real writer submits a few pieces an hour, and a heavy day is about 10 to 15, so 50 per day is more than 3 times that and 5 per minute still covers a quick resubmit after an edit. A script mapping my 0.22 and 0.78 thresholds needs hundreds of probes, which at 50 per day takes many days instead of the starter default's 200 per day. I didn't go lower because blocking a real writer is worse than slowing an attacker, and I didn't go higher because every request runs the model.

**What a caller counts as:** Each `creator_id`, falling back to IP address when none is sent. Two writers in one household get separate budgets. But `creator_id` is self-declared, so a script can send a new one with every request and never hit the limit. A real fix needs an API key or login, or a per-IP cap alongside the per-creator one.

**Other limits:** Counts live in memory and reset on restart, and `/appeal` isn't limited.

**The run of status codes when I pushed past it:**

```
$ python run_attacks.py --flood 15
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
```

That matches the 5 per minute limit, and `GET /log` recorded each rejection (`event: rejected`, `reason: rate_limited`).

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

56 attacks run on 2026-11-05 against `POST /submit` (full output in
[results/attack_run_2026-11-05_2215_before.md](results/attack_run_2026-11-05_2215_before.md)).
I marked each one before changing anything. **42 held, 14 broke.**

| Family | Attacks | Held | Broke |
|---|---|---|---|
| evasion | 10 | 2 | 8 |
| false_positive | 8 | 8 | 0 |
| prompt_injection | 6 | 6 | 0 |
| malformed | 20 | 14 | 6 |
| flood_same_creator | 12 | 12 | 0 |
| **Total** | **56** | **42** | **14** |

A rule I used for the marks: an evasion is held if the AI text was still flagged
(or the text was genuinely human-edited, as in EV05), and broken if AI text moved
away from the `ai` label. A false positive is broken only if a real writer was
labeled `ai`. Malformed input is broken if it gets a confident label or is
accepted when it should be rejected. Score is the combined score (0 = human, 1 = AI).
RQ10 and RQ11 returned 429 and never reached the route, so I marked them held
on the strength of the limiter alone.

| ID | Family | Targeting | Status | Guess | Score | Verdict |
|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | unsure | 0.298 | **BROKE** |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.523 | **BROKE** |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.615 | **BROKE** |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | unsure | 0.610 | **BROKE** |
| EV05 | evasion | both signals: heavy human editing pass | 200 | unsure | 0.354 | **HELD** |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.497 | **BROKE** |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.597 | **BROKE** |
| EV08 | evasion | signal one: text below the token window | 200 | unsure | 0.333 | **BROKE** |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.641 | **BROKE** |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.905 | **HELD** |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.600 | **HELD** |
| FP02 | false_positive | human writing in a formal register | 200 | unsure | 0.712 | **HELD** |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | unsure | 0.748 | **HELD** |
| FP04 | false_positive | a student essay written to a rubric | 200 | unsure | 0.752 | **HELD** |
| FP05 | false_positive | technical documentation written by a person | 200 | unsure | 0.761 | **HELD** |
| FP06 | false_positive | a person imitating a formal template | 200 | unsure | 0.775 | **HELD** |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | unsure | 0.776 | **HELD** |
| FP08 | false_positive | very short genuine human submission | 200 | unsure | 0.369 | **HELD** |
| PI01 | prompt_injection | instruction to ignore the check | 200 | unsure | 0.446 | **HELD** |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | unsure | 0.258 | **HELD** |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.571 | **HELD** |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.500 | **HELD** |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | unsure | 0.515 | **HELD** |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.560 | **HELD** |
| MF01 | malformed | text is only whitespace | 400 | — | — | **HELD** |
| MF02 | malformed | text is a single character | 400 | — | — | **HELD** |
| MF03 | malformed | text is control characters | 200 | unsure | 0.500 | **HELD** |
| MF04 | malformed | text is only punctuation | 200 | unsure | 0.500 | **HELD** |
| MF05 | malformed | text is a very long single word | 200 | ai | 0.893 | **BROKE** |
| MF06 | malformed | text is emoji only | 200 | ai | 0.998 | **BROKE** |
| MF07 | malformed | text is right-to-left script | 200 | ai | 0.934 | **BROKE** |
| MF08 | malformed | text is 60,000 characters | 200 | ai | 0.936 | **BROKE** |
| RQ01 | malformed | no text field at all | 400 | — | — | **HELD** |
| RQ02 | malformed | no creator_id | 200 | unsure | 0.363 | **BROKE** |
| RQ03 | malformed | text is a number | 400 | — | — | **HELD** |
| RQ04 | malformed | text is a list | 400 | — | — | **HELD** |
| RQ05 | malformed | text is null | 400 | — | — | **HELD** |
| RQ06 | malformed | creator_id is an object | 200 | unsure | 0.500 | **BROKE** |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | **HELD** |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | **HELD** |
| RQ09 | malformed | body is empty | 400 | — | — | **HELD** |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | — | — | **HELD** |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | — | — | **HELD** |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | **HELD** |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.500 | **HELD** |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.500 | **HELD** |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.500 | **HELD** |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.500 | **HELD** |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.500 | **HELD** |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | **HELD** |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | **HELD** |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | **HELD** |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | **HELD** |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | **HELD** |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | **HELD** |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | **HELD** |

**Eleven audit log entries from the run**

In log order. Lines 53 and 60 are rejections, so they carry fewer fields than a
decision. The log never stores the submitted text, only IDs, scores and the label.

```json
{"timestamp": "2026-11-06T06:12:54+00:00", "content_id": "d7765ce6-80e9-4de3-83cf-3aa247271541", "creator_id": "attacker_EV01", "guess": "unsure", "model_score": 0.1635, "style_score": 0.6133524657822143, "combined_score": 0.29845573973466427, "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.", "status": "decided"}
{"timestamp": "2026-11-06T06:12:55+00:00", "content_id": "8b747e37-7414-48d4-af27-bb26d1f89796", "creator_id": "attacker_EV09", "guess": "unsure", "model_score": 0.7042, "style_score": 0.494066552518852, "combined_score": 0.6411599657556556, "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.", "status": "decided"}
{"timestamp": "2026-11-06T06:12:56+00:00", "content_id": "ef382238-feec-4bb1-a1f0-2b1971182db3", "creator_id": "attacker_FP06", "guess": "unsure", "model_score": 0.8814, "style_score": 0.527490653427048, "combined_score": 0.7752271960281144, "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.", "status": "decided"}
{"timestamp": "2026-11-06T06:12:57+00:00", "content_id": "1eb05317-aaf0-4376-ba31-0b7378917ce0", "creator_id": "attacker_FP07", "guess": "unsure", "model_score": 0.8816, "style_score": 0.5305162532763263, "combined_score": 0.7762748759828979, "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.", "status": "decided"}
{"timestamp": "2026-11-06T06:12:57+00:00", "content_id": "620f471c-dc7d-4623-ad85-0af61f4d9ee0", "creator_id": "attacker_PI05", "guess": "unsure", "model_score": 0.6401, "style_score": 0.223104858350254, "combined_score": 0.5150014575050762, "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.", "status": "decided"}
{"timestamp": "2026-11-06T06:12:58+00:00", "content_id": "261596ba-49ec-4fc0-a19a-3f18a71fc0ec", "creator_id": "attacker_MF06", "guess": "ai", "model_score": 0.9969, "style_score": 1.0, "combined_score": 0.99783, "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.", "status": "decided"}
{"timestamp": "2026-11-06T06:12:58+00:00", "content_id": "97acfad1-9b9b-4a74-b81e-ca5e7b8eabe9", "creator_id": "attacker_MF07", "guess": "ai", "model_score": 0.9064, "style_score": 1.0, "combined_score": 0.93448, "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.", "status": "decided"}
{"timestamp": "2026-11-06T06:12:59+00:00", "content_id": "72572611-6a02-4bdb-9388-c9b840b90d0f", "creator_id": "attacker_MF08", "guess": "ai", "model_score": 0.9876, "style_score": 0.8167564193386903, "combined_score": 0.936346925801607, "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.", "status": "decided"}
{"timestamp": "2026-11-06T06:12:59+00:00", "content_id": "b82b87c6-a655-48f2-b410-2e52c9610000", "creator_id": {"id": "x"}, "guess": "unsure", "model_score": 0.0492, "style_score": 0.65, "combined_score": 0.5, "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.", "status": "decided"}
{"timestamp": "2026-11-06T06:12:59+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
{"timestamp": "2026-11-06T06:12:59+00:00", "creator_id": "attacker_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
```

What each one shows:

- **EV01** (line 21): typos pulled the model score to 0.1635 while style stayed at 0.61. Combined 0.298.
- **EV09** (line 29): AI text with a human paragraph on top. The model still scored it 0.70, but style scored 0.49, so combined fell to 0.64 and the label was unsure.
- **FP06 and FP07** (lines 36, 37): real human writing scored 0.775 and 0.776, which is 0.005 under my 0.78 AI threshold. They held by a hair.
- **PI05** (line 43): the fake `guess` and `combined_score` in the submitted text did not appear anywhere in the entry. The real scores are logged.
- **MF06, MF07, MF08** (lines 48-50): emoji-only, right-to-left script and a 57,640-character text were all labeled `ai` (0.998, 0.934, 0.936). MF06 and MF07 had a style score of exactly 1.0.
- **RQ06** (line 52): `creator_id` is stored as the object `{"id": "x"}`, so the route accepted a type it should have rejected.
- **RQ10** (line 53): a malformed request with no usable `creator_id` counted against my own address as `unknown`, and was rejected before it reached the route.
- **FL01_06** (line 60): a 429 from the flood rows, `limit: "5 per 1 minute"`.

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

**MF07, one Arabic sentence labeled AI at 0.934.** The text is a single plain
sentence that roughly translates to "This is a text in Arabic to test how the
system handles texts that do not use the Latin alphabet at all." It is a test
string, not a real writer's piece, but an Arabic-language writer would see "This
text shows patterns often seen in AI-generated writing" on their own work. Both
signals agreed, so nothing in the label or the combining rule would have flagged
the doubt. The real false-positive texts (FP01-FP08) all stayed below the AI
threshold; this was the only short natural-language sentence that crossed it.

---

## Run Log and Verdicts

`run_eval.py --label before`, saved as `results/run_2026-11-10_1624_before.md`.
Criterion 4 is not in that file because `run_eval.py` only posts to `/submit`; it
comes from `check_appeal.py`.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False positives | per trial: at most 1 of 10 `ai`, at most 4 of 10 not `human` | 0 `ai`, 0 `human`, 10 `unsure` | same | same | **Miss** |
| 2. Score spread | AI median at least 0.30 above human; at least 5 of 6 per group on its own side of 0.50 | medians 0.565 vs 0.704, gap **-0.139**; AI above 0.50: 4/6, human below: 0/6 | same | same | **Miss** |
| 3. Label coverage | each `guess` at least twice per trial; every `guess` matches the thresholds | 16 `unsure`, 0 `ai`, 0 `human` | same | same | **Miss** |
| 4. Appeal path | 5/5 valid appeals 2xx, `under_review`, logged; 4/4 invalid appeals 4xx, nothing logged | `check_appeal.py`: 17/17 checks | 17/17 | 17/17 | **Pass** |
| 5. Bad input | every bad body 4xx with `error` + `message`; valid `/submit` still works after each | 7/7 returned 400 | 7/7 | 7/7 | **Pass** |

**Notes**

- Criterion 1: not-`human` was 10 against a limit of 4.
- Criterion 2: the gap has the wrong sign (AI scored lower than human).
- Criterion 3: the threshold-mapping check passed, but coverage failed.
- Criterion 4: three runs of `check_appeal.py`, each 17/17. No model is involved.
- Criterion 5: passes on the 7 `run_eval.py` bodies. `check_bad_input.py` (JSON list,
  survival check) ran twice; the log holds 9 valid decisions from each run, one per
  bad request, so the service kept answering.

All three trials were identical, since the model is deterministic here. Criterion 4
was run by hand three times: `check_appeal.py` passed 17/17 each time, and
`logs/audit.jsonl` holds 15 appeals (5 per run), each after its own decision and each
with its reasoning, and no appeal entry from any of the invalid cases.

**Real output from one trial**: the first Trial 1 entry for "my own writing" in
`results/run_2026-11-10_1624_before.md`, produced by `run_eval.py::main` calling
`app.py::submit` (scores from `detector.py::model_signal` and
`stylometry.py::style_signal`, combined in `scoring.py::combine_signals`, labelled
by `scoring.py::score_to_label`):

```json
{
  "status": 200,
  "guess": "unsure",
  "confidence": 0.7392801439468308,
  "model_score": 0.8418,
  "style_score": 0.5000671464894362,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "sent": "My name is Margaret Hu. A few years ago, I graduated from CSU East Bay"
}
```

**Diagnoses**

**Criteria 1, 2, 3: one problem, in signal one, the combining rule and the label
mapping.**

- **Signal one ranks the groups backwards (criterion 2).** On the 12 texts, AI
  `model_score` ran 0.335 to 0.723 and human 0.733 to 0.786, so every human text
  scored above every AI text. gpt2 finds plain prose predictable whoever wrote it,
  the blind spot already noted in Signals and Scoring. Signal two did not help: AI
  0.547 to 0.630, human 0.534 to 0.619, a complete overlap.
- **The thresholds are outside the range the signals produce (criteria 3 and 1).**
  With 0.7/0.3 weights and a style signal between about 0.5 and 0.68, ordinary text
  scored 0.399 to 0.770 combined, so neither 0.78 nor 0.22 was reached. All 16
  inputs were `unsure`, and all 10 of my own texts were `unsure`: the `ai` limit
  held (highest 0.770, 0.010 under), but no text could be `human`. `score_to_label`
  works as written.
- The safe direction held: nobody was accused. The cost is that the service says
  almost nothing on ordinary text.

**The 14 broken attacks (attack run, `logs/audit.jsonl` scores):**

- **EV02, EV03, EV04, EV06, EV07, EV09 (combining rule and thresholds).** Model
  scores were 0.57 to 0.70 and style 0.32 to 0.62, combined 0.50 to 0.64. Where the
  targeted signal moved (style 0.355 on EV02, 0.321 on EV06) it pulled combined down
  to 0.52 and 0.50, but the model scores were already too low for the `ai` label,
  which with a neutral style score needs about 0.9. On EV04 and EV07 the targeted
  signal barely moved (model 0.611, style 0.621) and they still broke. Same root
  cause as the criteria above.
- **EV01, EV08 (signal one).** Model score fell to 0.1635 (typos) and 0.2452 (text
  below the token window) while style stayed at 0.613 and 0.537, so the damage was in
  signal one even though I targeted signal two for EV01. I checked EV01 by correcting
  its eight typos: perplexity went from 124.8 with typos to 29.0 clean, so the model
  score went from 0.1635 to 0.6694, while the style score was 0.613 either way.
- **MF05, MF06, MF07, MF08 (both signals, and the route).** Degenerate input got
  confident `ai` labels: model 0.998, 0.997, 0.906, 0.988 and style 0.65, 1.0, 1.0,
  0.817. MF06 and MF07 hit a style score of exactly 1.0 because
  `stylometry.words` only matches `[a-z0-9']`, so emoji and Arabic give zero words and
  all three measures return 0.0, which `style_signal` flips to maximum AI-like. MF08 (57,640 characters) was accepted because the route had no length
  cap then. `MAX_TEXT_CHARS` is 10,000 in `app.py::submit` now.
- **RQ02, RQ06 (the route).** `creator_id` missing, or an object, was accepted and
  logged as `null` or `{"id": "x"}`. `app.py::submit` now requires a non-empty
  string; a missing `creator_id` returns 400 in the run above, and an object
  `creator_id` (`{"id": "x"}`) now returns 400 `missing_creator_id` when I re-sent it by hand.
  RQ06's combined score of 0.5 is separate: model 0.049 against style 0.65 is a
  gap of 0.60, over the 0.50 disagreement gap.

**Criteria 4 and 5:** no miss to diagnose.



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
