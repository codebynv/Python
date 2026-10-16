# Test Isolation

- Use temporary directories for filesystem tests.
- Replace network calls with controlled fixtures in unit tests.
- Reset shared state between tests.
- Keep test data deterministic.
- Make cleanup reliable even when a test fails.
- Separate unit tests from integration tests that need external services.

A test should be repeatable on a clean checkout.
