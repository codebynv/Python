# Command-Line Interface Design

- Provide a concise help message.
- Validate arguments before doing work.
- Write diagnostics to stderr when appropriate.
- Use meaningful exit codes.
- Avoid destructive defaults.
- Keep output stable enough for scripts when machine-readable output is offered.

Test missing arguments, invalid values, and filesystem errors.