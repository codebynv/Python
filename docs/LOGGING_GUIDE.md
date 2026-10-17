# Python Logging Guide

- Use the logging module instead of scattered debug prints in maintained applications.
- Choose appropriate severity levels.
- Include useful context without sensitive values.
- Avoid logging secrets, tokens, or full private payloads.
- Keep messages actionable.
- Test error paths as well as successful execution.

Library code should generally let the application configure logging handlers.
