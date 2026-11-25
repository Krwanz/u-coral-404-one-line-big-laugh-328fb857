#!/usr/bin/env python3
"""One Line, Big Laugh — writes a single funny line to /output/entry.txt.

The program takes no input and needs no network: it writes one line of
at most 200 characters, then exits.
"""

import os

LINE = "My grandfather left me his watch, his war stories, and a restraining order against a goose he swore was a government drone."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
