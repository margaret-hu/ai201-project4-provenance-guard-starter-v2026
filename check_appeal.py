#!/usr/bin/env python3
"""
Criterion 4, the appeal path, which run_eval.py can't do (it only posts to /submit).

    python app.py              # in one terminal
    python check_appeal.py     # in another

Part 1: for each of 5 texts (two AI, two human, one of my own writing), submit
it, appeal the content_id that comes back with its own reasoning, and check:

  - /appeal returns 2xx with status "under_review" and the same content_id
  - /log has exactly one decision and one appeal for that id, the decision comes
    first and is still "decided", and the appeal keeps the reasoning

Part 2: 4 invalid appeals (unknown content_id, missing content_id, empty
reasoning, whitespace-only reasoning) plus two extras (empty content_id, a JSON
list). Each must return a 4xx with a JSON `error` and `message` and write no
appeal entry.
"""

import sys
import uuid

import requests

import config
import scenarios

BASE = f"http://{config.HOST}:{config.PORT}"

SPREAD = next(s for s in scenarios.SCENARIOS if s["criterion"] == 2)["texts"]
OWN = next(s for s in scenarios.SCENARIOS if s["criterion"] == 1)["texts"]

# (description, text). SPREAD is 6 AI texts then 6 human texts.
TEXTS = [
    ("AI text 1", SPREAD[0]),
    ("AI text 2", SPREAD[3]),
    ("human text 1", SPREAD[6]),
    ("human text 2", SPREAD[9]),
    ("my own writing", OWN[0]),
]

results = []


def check(name, ok, detail=""):
    results.append(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))


def entries_for(content_id):
    log = requests.get(f"{BASE}/log", timeout=30).json()["entries"]
    return [e for e in log if e.get("content_id") == content_id]


def appeals_for(content_id):
    return [e for e in entries_for(content_id) if e.get("event") == "appeal"]


def clean_error(r, status=None):
    try:
        data = r.json()
    except ValueError:
        return False
    return (isinstance(data, dict) and "error" in data and "message" in data
            and (r.status_code == status if status else 400 <= r.status_code < 500))


def valid_appeal(n, desc, text):
    creator = f"check_appeal_{uuid.uuid4().hex[:8]}"
    s = requests.post(f"{BASE}/submit", json={"text": text, "creator_id": creator}, timeout=90)
    content_id = s.json().get("content_id") if s.status_code == 200 else None
    if not content_id:
        check(f"[{n}] {desc}: submit returns a content_id", False, f"status {s.status_code}")
        return None

    reasoning = f"Appeal {n}: I believe this ({desc}) was misjudged."
    a = requests.post(f"{BASE}/appeal", timeout=30,
                      json={"content_id": content_id, "reasoning": reasoning})
    try:
        body = a.json()
    except ValueError:
        body = {}
    check(f"[{n}] {desc}: appeal 2xx, under_review, same content_id",
          200 <= a.status_code < 300 and body.get("status") == "under_review"
          and body.get("content_id") == content_id,
          f"status {a.status_code}")

    mine = entries_for(content_id)
    decision = [e for e in mine if e.get("event") != "appeal"]
    appeal = [e for e in mine if e.get("event") == "appeal"]
    ok = (len(decision) == 1 and len(appeal) == 1
          and mine.index(decision[0]) < mine.index(appeal[0])
          and decision[0].get("status") == "decided"
          and appeal[0].get("status") == "under_review"
          and appeal[0].get("reasoning") == reasoning
          and appeal[0].get("creator_id") == creator)
    check(f"[{n}] {desc}: log has decision (unchanged) then appeal with reasoning", ok,
          f"{len(decision)} decision, {len(appeal)} appeal, "
          f"decision status {decision[0].get('status') if decision else None}")
    return content_id


def main():
    ids = [valid_appeal(i, d, t) for i, (d, t) in enumerate(TEXTS, 1)]
    ids = [i for i in ids if i]
    if not ids:
        sys.exit(1)
    real = ids[0]
    unknown = str(uuid.uuid4())

    # (name, body, expected status or None for any 4xx, id whose appeals must not grow)
    cases = [
        ("unknown content_id -> 404", {"content_id": unknown, "reasoning": "x"}, 404, unknown),
        ("missing content_id", {"reasoning": "x"}, None, None),
        ("empty reasoning", {"content_id": real, "reasoning": ""}, None, real),
        ("whitespace-only reasoning", {"content_id": real, "reasoning": " \n\t "}, None, real),
        ("extra: empty content_id", {"content_id": "", "reasoning": "x"}, None, None),
        ("extra: json list body", [{"content_id": real, "reasoning": "x"}], None, real),
    ]
    total_before = len(requests.get(f"{BASE}/log", timeout=30).json()["entries"])
    for name, body, status, watch in cases:
        before = len(appeals_for(watch)) if watch else 0
        r = requests.post(f"{BASE}/appeal", json=body, timeout=30)
        after = len(appeals_for(watch)) if watch else 0
        check(f"invalid: {name}", clean_error(r, status) and after == before,
              f"status {r.status_code}, appeals for id {before} -> {after}")
    total_after = len(requests.get(f"{BASE}/log", timeout=30).json()["entries"])
    check("invalid appeals added nothing to the log", total_after == total_before,
          f"{total_before} -> {total_after}")

    passed = sum(results)
    print(f"\n{passed}/{len(results)} passed")
    sys.exit(0 if passed == len(results) else 1)


if __name__ == "__main__":
    main()
