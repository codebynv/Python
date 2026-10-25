# Test Failure Diagnosis

When a test fails:

1. Read the complete assertion and traceback.
2. Reproduce the failure in isolation if practical.
3. Check whether the fixture or environment changed.
4. Identify the smallest relevant behavior change.
5. Add a regression case for a confirmed defect.
6. Rerun the focused test and the relevant suite.

Do not weaken assertions simply to make a failing suite pass.
