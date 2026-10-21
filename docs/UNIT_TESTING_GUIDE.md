# Unit Testing Guide

- Keep each test focused on one behavior.
- Use descriptive test names.
- Cover normal input, boundaries, and expected failures.
- Replace network and filesystem dependencies when isolation is useful.
- Prefer deterministic fixtures over shared mutable state.
- Test public behavior rather than implementation details.
- Run the configured test command before submitting changes.

Only describe tests as passing after running them.