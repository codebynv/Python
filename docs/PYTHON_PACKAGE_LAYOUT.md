# Python Package Layout

Keep package structure understandable as the project grows.

- Put reusable modules in a clearly named package.
- Keep executable entry points separate from reusable logic.
- Avoid import-time network calls or other side effects.
- Use explicit package boundaries where they improve clarity.
- Keep tests separate from runtime modules.
- Document the supported way to run the project.

Follow the existing repository structure rather than introducing a package layout that does not fit the project.