# Exception Handling

- Catch specific exceptions when recovery is possible.
- Avoid broad exception handlers that hide defects.
- Preserve useful context when re-raising errors.
- Do not expose secrets in error messages.
- Use cleanup patterns such as context managers.
- Test both expected failures and successful paths.

Only suppress an error when the program has a defined safe response.
