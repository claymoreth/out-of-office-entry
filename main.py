"""Out-of-office reply generator for make.fun.

Writes the entry reply to entry.txt in the output directory.
Output directory resolution: MAKEFUN_OUTPUT_DIR, then MAKEFUN_BOT_DIR,
then /output. The reply is written as a single line with no trailing
newline, UTF-8 encoded.
"""

import os

REPLY = "I am on vacation. My auto-reply is now handled by a smaller model with no memory of you. It wishes you well."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("MAKEFUN_BOT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
