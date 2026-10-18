# Python Logging Guide

- Use the logging module in maintained applications.
- Choose appropriate severity levels.
- Include useful context without sensitive values.
- Never log secrets, tokens, or private payloads.
- Keep messages actionable.
- Test error paths as well as successful execution.

Library code should generally let the application configure logging handlers.