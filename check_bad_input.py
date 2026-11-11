#!/usr/bin/env python3
"""
Criterion 5, the parts run_eval.py can't do.

    python app.py                  # in one terminal
    python check_bad_input.py      # in another

Sends every bad request (the "bad input" scenario's bodies plus a bare JSON
list), and after EACH one sends a valid /submit. Checks that:

  1. the bad request gets a 4xx with a JSON `error` and `message`
  2. the valid request right after it still gets a 200

Each valid request uses its own creator_id so the rate limit never confuses
the result.
"""

import sys
import uuid

import requests

import config
import scenarios

URL = f"http://{config.HOST}:{config.PORT}/submit"

VALID_TEXT = (
    "I heard Martha and Scott are hosting a Christmas caroling party on "
    "December 22. There will be lots of food and hot drinks, so you don't "
    "need to bring anything unless you have a dish or dessert you want to share."
)

# The "bad input" scenario's bodies, plus the one a dict can't express.
BAD = [(b.get("creator_id", "(no creator_id)"), b)
       for s in scenarios.SCENARIOS for b in s.get("bodies", [])]
BAD += [("json list", [{"text": VALID_TEXT, "creator_id": "x"}]),
        ("json string", "just a string")]


def main():
    failures = 0
    for name, body in BAD:
        r = requests.post(URL, json=body, timeout=90)
        try:
            data = r.json()
        except ValueError:
            data = None
        rejected = (400 <= r.status_code < 500 and isinstance(data, dict)
                    and "error" in data and "message" in data)

        v = requests.post(URL, json={"text": VALID_TEXT,
                                     "creator_id": f"check_{uuid.uuid4().hex[:8]}"},
                          timeout=90)
        alive = v.status_code == 200

        ok = rejected and alive
        failures += not ok
        print(f"{'PASS' if ok else 'FAIL'}  {name:<26} bad->{r.status_code} "
              f"{'(error+message)' if rejected else '(NOT a clean 4xx)'}  "
              f"next valid->{v.status_code}")

    print(f"\n{len(BAD) - failures}/{len(BAD)} passed")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
