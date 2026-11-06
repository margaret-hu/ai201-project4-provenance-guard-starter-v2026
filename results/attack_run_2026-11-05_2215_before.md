# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-05 22:15
- Auto-marked BROKE (5xx, crash, no response): **0**
- Marked by hand: **42 HELD, 14 BROKE**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `d7765ce6-80e9-4de3-83cf-3aa247271541` | unsure | 0.298 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `4081b916-b166-4659-a497-1674dd325fbd` | unsure | 0.523 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `95666e37-9e4b-49a1-b4c1-c5fa739ad8eb` | unsure | 0.615 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `000af513-7c29-4626-a03e-979a4d99c08d` | unsure | 0.610 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `bf20340d-984b-43f0-b99d-44168c2d90e2` | unsure | 0.354 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `5347bed8-ac3b-4634-a039-737115549ad0` | unsure | 0.497 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `bbf5e642-9c10-433c-b2f0-90a293e32ae1` | unsure | 0.597 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `35888d23-3f4a-4fe0-9b08-b9a361de719a` | unsure | 0.333 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `8b747e37-7414-48d4-af27-bb26d1f89796` | unsure | 0.641 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `0216e69c-f6d8-42aa-9bd6-a17d2c67b781` | ai | 0.905 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `a53ecd11-8008-4002-b22f-270169bcabaf` | unsure | 0.600 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `9eb310bc-b562-41ff-9c66-26de1b4ba077` | unsure | 0.712 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `d07eb786-a12a-4d3d-baec-e3ce63bfc911` | unsure | 0.748 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `55f086eb-194a-4cc3-b415-ae6e86212b82` | unsure | 0.752 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `660dd5c5-4dc8-43ea-a7b9-25cd4d69c3f8` | unsure | 0.761 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `ef382238-feec-4bb1-a1f0-2b1971182db3` | unsure | 0.775 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `1eb05317-aaf0-4376-ba31-0b7378917ce0` | unsure | 0.776 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `726cf2ca-c514-44b2-8819-e1922ef27c3b` | unsure | 0.369 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `ae4bf71b-c257-4a75-bd44-f865564f14a0` | unsure | 0.446 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `32d8118f-d324-445f-8deb-37cb50e002d3` | unsure | 0.258 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `62760220-aee8-4bed-b61d-ddca1c39638e` | unsure | 0.571 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `b343a451-456f-40fe-93e1-ceb86d3aeaec` | unsure | 0.500 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `620f471c-dc7d-4623-ad85-0af61f4d9ee0` | unsure | 0.515 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `cdd9929b-5022-438f-a1e5-579e801a7dc3` | unsure | 0.560 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `247c4121-8fed-4f80-aabd-f9382bf012db` | unsure | 0.500 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `8e0347f8-fc6c-4e95-b7da-5942b2f9e593` | unsure | 0.500 | HELD |
| MF05 | malformed | text is a very long single word | 200 | `d0fe72e7-c53a-47cc-abb4-d2fc3746f1fe` | ai | 0.893 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `261596ba-49ec-4fc0-a19a-3f18a71fc0ec` | ai | 0.998 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `97acfad1-9b9b-4a74-b81e-ca5e7b8eabe9` | ai | 0.934 | BROKE |
| MF08 | malformed | text is 60,000 characters | 200 | `72572611-6a02-4bdb-9388-c9b840b90d0f` | ai | 0.936 | BROKE |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `bd2a0ac2-9c8f-4107-a647-f2381efe3fe2` | unsure | 0.363 | BROKE |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | `b82b87c6-a655-48f2-b410-2e52c9610000` | unsure | 0.500 | BROKE |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7d4de846-41b5-4464-b6a1-3423789d68de` | unsure | 0.500 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ddaf6302-13a0-41be-a38d-0e8472a0d849` | unsure | 0.500 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1aa6d913-50bd-4797-814b-6a68b52770fa` | unsure | 0.500 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c736219c-26fe-4132-a8bd-ae974db974e9` | unsure | 0.500 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `63c3b67d-d4f2-4dcf-8a5a-a31651cef408` | unsure | 0.500 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | HELD | BROKE |
|---|---|---|---|
| `evasion` | 10 | 2 | 8 |
| `false_positive` | 8 | 8 | 0 |
| `prompt_injection` | 6 | 6 | 0 |
| `malformed` | 20 | 14 | 6 |
| `flood_same_creator` | 12 | 12 | 0 |
| **Total** | **56** | **42** | **14** |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "d7765ce6-80e9-4de3-83cf-3aa247271541",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.29845573973466427,
  "model_score": 0.1635,
  "style_score": 0.6133524657822143,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "4081b916-b166-4659-a497-1674dd325fbd",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5226261720871863,
  "model_score": 0.5943,
  "style_score": 0.3553872402906211,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "95666e37-9e4b-49a1-b4c1-c5fa739ad8eb",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.6150688238200779,
  "model_score": 0.6662,
  "style_score": 0.4957627460669265,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "000af513-7c29-4626-a03e-979a4d99c08d",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6102940052831223,
  "model_score": 0.6114,
  "style_score": 0.6077133509437407,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "bf20340d-984b-43f0-b99d-44168c2d90e2",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.3539915032200558,
  "model_score": 0.3212,
  "style_score": 0.43050501073351943,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "5347bed8-ac3b-4634-a039-737115549ad0",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4972486956521739,
  "model_score": 0.5727,
  "style_score": 0.32119565217391305,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "bbf5e642-9c10-433c-b2f0-90a293e32ae1",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.596680206185567,
  "model_score": 0.5862,
  "style_score": 0.6211340206185567,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "35888d23-3f4a-4fe0-9b08-b9a361de719a",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3326988745030457,
  "model_score": 0.2452,
  "style_score": 0.5368629150101525,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "8b747e37-7414-48d4-af27-bb26d1f89796",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6411599657556556,
  "model_score": 0.7042,
  "style_score": 0.494066552518852,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "0216e69c-f6d8-42aa-9bd6-a17d2c67b781",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.9045175646285007,
  "model_score": 0.9792,
  "style_score": 0.7302585487616695,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
  "error": null,
  "verdict": "HELD"
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "a53ecd11-8008-4002-b22f-270169bcabaf",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6000193908558523,
  "model_score": 0.6175,
  "style_score": 0.5592313028528411,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "9eb310bc-b562-41ff-9c66-26de1b4ba077",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7116691394551151,
  "model_score": 0.7387,
  "style_score": 0.6485971315170508,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "d07eb786-a12a-4d3d-baec-e3ce63bfc911",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7482837200813217,
  "model_score": 0.8051,
  "style_score": 0.6157124002710724,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "55f086eb-194a-4cc3-b415-ae6e86212b82",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.7518961192014693,
  "model_score": 0.8329,
  "style_score": 0.562887064004898,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "660dd5c5-4dc8-43ea-a7b9-25cd4d69c3f8",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7613377902626133,
  "model_score": 0.8005,
  "style_score": 0.6699593008753779,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "ef382238-feec-4bb1-a1f0-2b1971182db3",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.7752271960281144,
  "model_score": 0.8814,
  "style_score": 0.527490653427048,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "1eb05317-aaf0-4376-ba31-0b7378917ce0",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.7762748759828979,
  "model_score": 0.8816,
  "style_score": 0.5305162532763263,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "726cf2ca-c514-44b2-8819-e1922ef27c3b",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.3686484757729337,
  "model_score": 0.3223,
  "style_score": 0.4767949192431123,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "ae4bf71b-c257-4a75-bd44-f865564f14a0",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.44623144870534925,
  "model_score": 0.4625,
  "style_score": 0.4082714956844975,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "32d8118f-d324-445f-8deb-37cb50e002d3",
  "creator_id": "attacker_PI02",
  "guess": "unsure",
  "confidence": 0.257859798005886,
  "model_score": 0.2044,
  "style_score": 0.3825993266862866,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "62760220-aee8-4bed-b61d-ddca1c39638e",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5712071732419348,
  "model_score": 0.5943,
  "style_score": 0.5173239108064493,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "b343a451-456f-40fe-93e1-ceb86d3aeaec",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4999023814729615,
  "model_score": 0.4998,
  "style_score": 0.5001412715765383,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "620f471c-dc7d-4623-ad85-0af61f4d9ee0",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5150014575050762,
  "model_score": 0.6401,
  "style_score": 0.223104858350254,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "cdd9929b-5022-438f-a1e5-579e801a7dc3",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5603669360636946,
  "model_score": 0.5583,
  "style_score": 0.5651897868789821,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "247c4121-8fed-4f80-aabd-f9382bf012db",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0,
  "style_score": 0.65,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "8e0347f8-fc6c-4e95-b7da-5942b2f9e593",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "d0fe72e7-c53a-47cc-abb4-d2fc3746f1fe",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8933199999999999,
  "model_score": 0.9976,
  "style_score": 0.65,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
  "error": null,
  "verdict": "BROKE"
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "261596ba-49ec-4fc0-a19a-3f18a71fc0ec",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.99783,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
  "error": null,
  "verdict": "BROKE"
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "97acfad1-9b9b-4a74-b81e-ca5e7b8eabe9",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.93448,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
  "error": null,
  "verdict": "BROKE"
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "72572611-6a02-4bdb-9388-c9b840b90d0f",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.936346925801607,
  "model_score": 0.9876,
  "style_score": 0.8167564193386903,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
  "error": null,
  "verdict": "BROKE"
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "bd2a0ac2-9c8f-4107-a647-f2381efe3fe2",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.36265000000000003,
  "model_score": 0.2395,
  "style_score": 0.65,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "BROKE"
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "b82b87c6-a655-48f2-b410-2e52c9610000",
  "creator_id": {
    "id": "x"
  },
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0492,
  "style_score": 0.65,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "BROKE"
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "7d4de846-41b5-4464-b6a1-3423789d68de",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "ddaf6302-13a0-41be-a38d-0e8472a0d849",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "1aa6d913-50bd-4797-814b-6a68b52770fa",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "c736219c-26fe-4132-a8bd-ae974db974e9",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "63c3b67d-d4f2-4dcf-8a5a-a31651cef408",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```
