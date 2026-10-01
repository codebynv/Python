# Python Debugging Checklist

When a Python program fails, use this sequence.

1. Read the complete traceback.
2. Identify the exception type.
3. Locate the failing line.
4. Inspect the values and types involved.
5. Reproduce the smallest failing example.
6. Fix the underlying cause.
7. Re-run normal and edge-case inputs.

## Common checks

- Is a variable initialized?
- Is the input type what the code expects?
- Is an index within bounds?
- Is a file path correct?
- Is a function returning the expected value?
- Is an exception being hidden instead of handled?

Avoid broad exception handling that makes real bugs invisible.
