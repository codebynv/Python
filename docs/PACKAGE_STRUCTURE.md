# Package Structure Notes

Keep Python modules organized around clear responsibilities.

## Guidelines

- Group related functionality into modules.
- Keep reusable functions independent from command-line entry points.
- Avoid circular imports.
- Keep configuration separate from implementation.
- Add tests around important reusable logic.

As the project grows, prefer clear package boundaries over one large module.
