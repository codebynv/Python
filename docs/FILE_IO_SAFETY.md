# Safe File I/O

- Use context managers to close files reliably.
- Specify text encodings when reading or writing text.
- Handle expected filesystem exceptions.
- Avoid overwriting user data without clear intent.
- Validate paths when processing untrusted input.
- Use temporary files for operations that should be atomic.

Test missing files, permission errors, empty files, and malformed content.
