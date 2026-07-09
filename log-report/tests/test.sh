#!/bin/bash
set -euo pipefail

# pytest and pytest-json-ctrf are baked into the environment image (environment/Dockerfile).
# No installs happen here.

mkdir -p /logs/verifier

pytest /tests/test_outputs.py \
  --json-report \
  --json-report-file=/logs/verifier/ctrf.json \
  -rA

EXIT=$?

if [ $EXIT -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

exit $EXIT
