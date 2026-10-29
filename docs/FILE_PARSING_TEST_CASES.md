# File Parsing Test Cases

For file-reading code, consider:

- a valid file,
- an empty file,
- malformed content,
- a missing file,
- an unexpected encoding,
- permission denied,
- a large file within and beyond the supported limit.

Handle expected failures explicitly and avoid leaking sensitive file contents in error messages. Verify behavior against the actual parser before claiming support.