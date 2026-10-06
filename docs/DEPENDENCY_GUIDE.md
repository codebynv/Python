# Dependency Guide

Keep project dependencies intentional.

## Rules

- Add a dependency only when it provides clear value.
- Pin or constrain versions when reproducibility requires it.
- Remove unused dependencies.
- Document unusual system-level requirements.
- Keep virtual environments outside version control.

After dependency changes, run the relevant tests and verify imports from a clean environment.
