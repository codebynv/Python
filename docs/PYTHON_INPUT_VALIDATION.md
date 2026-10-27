# Python Input Validation

For functions that accept external input:

- Define accepted types and ranges.
- Handle empty and whitespace-only strings intentionally.
- Reject malformed paths or values where applicable.
- Keep error messages actionable without leaking sensitive data.
- Test boundaries and unexpected types.
- Avoid silently converting invalid input to a plausible default.

Validate at system boundaries while keeping internal function contracts simple.