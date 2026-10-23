# Deterministic Tests

Tests should produce the same result across repeated runs.

- Fix random seeds when randomness is part of the test.
- Freeze time when asserting time-dependent behavior.
- Use temporary directories for filesystem tests.
- Stub network calls rather than relying on live services.
- Avoid order-dependent shared state.
- Clean up resources after each test.

Investigate flaky tests instead of adding retries that hide the cause.