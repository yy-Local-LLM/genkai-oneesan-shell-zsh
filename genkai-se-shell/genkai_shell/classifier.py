import re

_PATTERNS = [
    (re.compile(r"command not found|not found$", re.I | re.M), "command_not_found"),
    (re.compile(r"permission denied|operation not permitted", re.I), "permission_denied"),
    (re.compile(r"no such file|file not found", re.I), "no_such_file"),
    (re.compile(r"syntax error|unexpected token|parse error", re.I), "syntax_error"),
    (re.compile(r"connection refused|network unreachable|no route to host", re.I), "network"),
    (re.compile(r"timed? ?out|connection timed", re.I), "timeout"),
    (re.compile(r"no space left|disk quota exceeded", re.I), "disk_full"),
    (re.compile(r"out of memory|cannot allocate memory|killed", re.I), "oom"),
    (re.compile(r"not a git repository|fatal:|merge conflict", re.I), "git"),
    (re.compile(r"docker.*error|cannot connect.*docker|no such container", re.I), "docker"),
]


def classify(stderr: str, code: int, command: str = "") -> str:
    for pattern, category in _PATTERNS:
        if pattern.search(stderr):
            return category
    head = command.split(maxsplit=1)[0] if command else ""
    if code == 127 or head in {"which", "whereis"}:
        return "command_not_found"
    if code == 126:
        return "permission_denied"
    if head in {"git"}:
        return "git"
    if head in {"docker", "podman", "docker-compose"}:
        return "docker"
    return "generic"

