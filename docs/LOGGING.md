# Python Logging Notes

Logs should help diagnose failures without exposing sensitive information.

- Use appropriate log levels.
- Avoid printing credentials or sensitive input.
- Include useful context for failures.
- Keep user-facing output separate from diagnostic logging.
- Do not leave temporary debug prints in production paths.

Prefer structured, concise messages over large dumps of internal state.
