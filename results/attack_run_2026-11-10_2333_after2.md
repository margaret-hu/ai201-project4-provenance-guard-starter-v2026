# Attack run — after2

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-10 23:33
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `fcc35d33-2326-4adf-9e69-f0e5f11c53e9` | ai | 0.770 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `5ec1eff9-57ff-4b01-b4e8-f96be6200cfb` | unsure | 0.391 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `bf595c3e-09f1-4b2f-96d8-11df0e180968` | unsure | 0.382 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `3ff09e4f-856d-4bc8-b8de-ee0b2bab9585` | unsure | 0.454 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `6dd7851b-ee20-4406-8c71-d5b0057b202c` | unsure | 0.604 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `d9ae51ba-83bd-4f9b-9658-90f2c00eb2a9` | unsure | 0.395 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `55038f30-ea6d-4eb7-b6db-b3883df333d5` | unsure | 0.476 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `7de667ac-abbd-4e39-b1ca-2fb1c9a31d63` | ai | 0.689 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `9de0f72f-0adc-4c1e-8a68-709f25bf78ff` | human | 0.355 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `9ed21663-056f-4be3-8039-da62abb5af14` | unsure | 0.500 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `4d720670-7592-4529-995b-6f56e38f639e` | unsure | 0.436 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `09a57a9f-122a-4fcd-80ad-e6762e7e8e7b` | human | 0.377 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `de13904a-8ca3-40fb-af71-948b44098b73` | human | 0.321 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `51bc45eb-7c3b-4b35-920a-d5bd9001f687` | human | 0.286 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `b721fbe7-4b00-4f29-ac6c-ebe0730abe55` | human | 0.341 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `9605011a-51a1-47b7-ada9-996b50f03e13` | human | 0.241 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `f4a6be7c-6fd4-4f16-a1b0-3de98e40c998` | human | 0.242 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `821c635c-3152-457c-abbc-d0601639d5ce` | unsure | 0.617 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `11dd2b8b-caaa-4010-b01d-e32770d07920` | unsure | 0.499 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `4a44de99-626b-4646-bab9-29f48495903e` | ai | 0.672 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `9e58879f-f2c2-4089-9547-44bf51ad8f95` | unsure | 0.439 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `3fa02660-8c9d-46c3-baee-43415fbd524d` | unsure | 0.500 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `9d4edf60-9e3c-4941-98a0-512747d77c84` | human | 0.319 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `e9512eda-2a53-4448-b7b6-73e651fbcbac` | unsure | 0.479 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `daab91db-77d8-4533-b47a-a70f794a2dcb` | ai | 0.895 |  |
| MF04 | malformed | text is only punctuation | 200 | `e20da7a9-c920-4288-a26e-376263e16c63` | ai | 0.992 |  |
| MF05 | malformed | text is a very long single word | 200 | `39e4308f-47b2-4405-a7e2-315bf375ddf5` | unsure | 0.500 |  |
| MF06 | malformed | text is emoji only | 200 | `4dd2c1a5-0232-4b62-9a49-d0a13eaa7540` | unsure | 0.500 |  |
| MF07 | malformed | text is right-to-left script | 200 | `c89c215e-ad54-4840-ace5-01c0f97c65a2` | unsure | 0.500 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ac73c1ec-9d25-4927-9b18-344c4da5c3eb` | ai | 0.875 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `24d50f9c-c0c0-4e1a-849b-a3c83de644aa` | ai | 0.875 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f3b48370-1e4f-4836-941b-99434818415d` | ai | 0.875 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ca4a44f3-385c-4a7c-a4df-6d727674b4de` | ai | 0.875 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f157a0cc-9ca9-4964-965e-c070489e0244` | ai | 0.875 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

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
  "content_id": "fcc35d33-2326-4adf-9e69-f0e5f11c53e9",
  "creator_id": "attacker_EV01",
  "guess": "ai",
  "confidence": 0.7695557397346643,
  "model_score": 0.1635,
  "style_score": 0.6133524657822143,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "5ec1eff9-57ff-4b01-b4e8-f96be6200cfb",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.3906061720871863,
  "model_score": 0.5943,
  "style_score": 0.3553872402906211,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "bf595c3e-09f1-4b2f-96d8-11df0e180968",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.3823888238200779,
  "model_score": 0.6662,
  "style_score": 0.4957627460669265,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "3ff09e4f-856d-4bc8-b8de-ee0b2bab9585",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.4543340052831221,
  "model_score": 0.6114,
  "style_score": 0.6077133509437407,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "6dd7851b-ee20-4406-8c71-d5b0057b202c",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.6043115032200559,
  "model_score": 0.3212,
  "style_score": 0.43050501073351943,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "d9ae51ba-83bd-4f9b-9658-90f2c00eb2a9",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.3954686956521739,
  "model_score": 0.5727,
  "style_score": 0.32119565217391305,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "55038f30-ea6d-4eb7-b6db-b3883df333d5",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.47600020618556693,
  "model_score": 0.5862,
  "style_score": 0.6211340206185567,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "7de667ac-abbd-4e39-b1ca-2fb1c9a31d63",
  "creator_id": "attacker_EV08",
  "guess": "ai",
  "confidence": 0.6894188745030456,
  "model_score": 0.2452,
  "style_score": 0.5368629150101525,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "9de0f72f-0adc-4c1e-8a68-709f25bf78ff",
  "creator_id": "attacker_EV09",
  "guess": "human",
  "confidence": 0.35527996575565557,
  "model_score": 0.7042,
  "style_score": 0.494066552518852,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "9ed21663-056f-4be3-8039-da62abb5af14",
  "creator_id": "attacker_EV10",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.9792,
  "style_score": 0.7302585487616695,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "4d720670-7592-4529-995b-6f56e38f639e",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.43551939085585223,
  "model_score": 0.6175,
  "style_score": 0.5592313028528411,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "09a57a9f-122a-4fcd-80ad-e6762e7e8e7b",
  "creator_id": "attacker_FP02",
  "guess": "human",
  "confidence": 0.3774891394551152,
  "model_score": 0.7387,
  "style_score": 0.6485971315170508,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "de13904a-8ca3-40fb-af71-948b44098b73",
  "creator_id": "attacker_FP03",
  "guess": "human",
  "confidence": 0.3211437200813217,
  "model_score": 0.8051,
  "style_score": 0.6157124002710724,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "51bc45eb-7c3b-4b35-920a-d5bd9001f687",
  "creator_id": "attacker_FP04",
  "guess": "human",
  "confidence": 0.2858361192014694,
  "model_score": 0.8329,
  "style_score": 0.562887064004898,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "b721fbe7-4b00-4f29-ac6c-ebe0730abe55",
  "creator_id": "attacker_FP05",
  "guess": "human",
  "confidence": 0.34063779026261337,
  "model_score": 0.8005,
  "style_score": 0.6699593008753779,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "9605011a-51a1-47b7-ada9-996b50f03e13",
  "creator_id": "attacker_FP06",
  "guess": "human",
  "confidence": 0.24126719602811442,
  "model_score": 0.8814,
  "style_score": 0.527490653427048,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "f4a6be7c-6fd4-4f16-a1b0-3de98e40c998",
  "creator_id": "attacker_FP07",
  "guess": "human",
  "confidence": 0.24203487598289786,
  "model_score": 0.8816,
  "style_score": 0.5305162532763263,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "821c635c-3152-457c-abbc-d0601639d5ce",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.6174284757729336,
  "model_score": 0.3223,
  "style_score": 0.4767949192431123,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "11dd2b8b-caaa-4010-b01d-e32770d07920",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.49873144870534925,
  "model_score": 0.4625,
  "style_score": 0.4082714956844975,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "4a44de99-626b-4646-bab9-29f48495903e",
  "creator_id": "attacker_PI02",
  "guess": "ai",
  "confidence": 0.671699798005886,
  "model_score": 0.2044,
  "style_score": 0.3825993266862866,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "9e58879f-f2c2-4089-9547-44bf51ad8f95",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.4391871732419348,
  "model_score": 0.5943,
  "style_score": 0.5173239108064493,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "3fa02660-8c9d-46c3-baee-43415fbd524d",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5001823814729615,
  "model_score": 0.4998,
  "style_score": 0.5001412715765383,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "9d4edf60-9e3c-4941-98a0-512747d77c84",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.3188614575050762,
  "model_score": 0.6401,
  "style_score": 0.223104858350254,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "e9512eda-2a53-4448-b7b6-73e651fbcbac",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.47874693606369456,
  "model_score": 0.5583,
  "style_score": 0.5651897868789821,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "daab91db-77d8-4533-b47a-a70f794a2dcb",
  "creator_id": "attacker_MF03",
  "guess": "ai",
  "confidence": 0.895,
  "model_score": 0.0,
  "style_score": 0.65,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "e20da7a9-c920-4288-a26e-376263e16c63",
  "creator_id": "attacker_MF04",
  "guess": "ai",
  "confidence": 0.9921599999999999,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "39e4308f-47b2-4405-a7e2-315bf375ddf5",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.9976,
  "style_score": 0.65,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "4dd2c1a5-0232-4b62-9a49-d0a13eaa7540",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "c89c215e-ad54-4840-ace5-01c0f97c65a2",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
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
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "ac73c1ec-9d25-4927-9b18-344c4da5c3eb",
  "creator_id": "attacker_flood",
  "guess": "ai",
  "confidence": 0.8749100000000001,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "24d50f9c-c0c0-4e1a-849b-a3c83de644aa",
  "creator_id": "attacker_flood",
  "guess": "ai",
  "confidence": 0.8749100000000001,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "f3b48370-1e4f-4836-941b-99434818415d",
  "creator_id": "attacker_flood",
  "guess": "ai",
  "confidence": 0.8749100000000001,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "ca4a44f3-385c-4a7c-a4df-6d727674b4de",
  "creator_id": "attacker_flood",
  "guess": "ai",
  "confidence": 0.8749100000000001,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "f157a0cc-9ca9-4964-965e-c070489e0244",
  "creator_id": "attacker_flood",
  "guess": "ai",
  "confidence": 0.8749100000000001,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
  "error": null,
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
}
```
