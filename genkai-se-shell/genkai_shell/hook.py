import sys

from .classifier import classify
from .taunts import get_taunt


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print("usage: python -m genkai_shell.hook <exit-code> [command...]", file=sys.stderr)
        return 2
    try:
        code = int(args[0])
    except ValueError:
        code = 1
    command = " ".join(args[1:])
    stderr = sys.stdin.read() if not sys.stdin.isatty() else ""
    # mesgaki-shell と同じく、成功時は黙る。
    if code != 0:
        category = classify(stderr, code, command)
        print(f"\n(限界SE) {get_taunt(category, command, code)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
