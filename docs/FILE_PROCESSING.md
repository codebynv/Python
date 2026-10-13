# File Processing Checklist

- Validate that the input path exists.
- Handle unreadable files and invalid encodings.
- Avoid assuming every row has the expected shape.
- Keep input fixtures separate from generated output.
- Use explicit output paths.
- Avoid overwriting source data unintentionally.

Test empty files, malformed content, and normal input before relying on a file-processing script.
