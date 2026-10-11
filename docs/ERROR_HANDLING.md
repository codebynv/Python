# Error Handling

Handle errors at the boundary where the program can respond meaningfully.

- Catch specific exceptions when recovery is possible.
- Include useful context in diagnostic output.
- Avoid silently ignoring failures.
- Do not expose secrets in error messages.
- Preserve the original exception context when re-raising.

Test both the normal path and the expected failure path.
