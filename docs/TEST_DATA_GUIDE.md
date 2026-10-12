# Test Data Guide

Use small, deterministic fixtures for unit tests.

- Include normal input and important edge cases.
- Keep personal or confidential data out of fixtures.
- Make fixture names describe the scenario.
- Avoid relying on network services for basic unit tests.
- Document the origin and license of external datasets.
- Keep generated test output separate from source fixtures.

Tests should be repeatable on another machine.
