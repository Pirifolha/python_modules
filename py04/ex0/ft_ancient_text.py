#!/usr/bin/env python3

import sys


def main() -> None:
    args: list[str] = sys.argv
    if len(args) == 1:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("== Cyber Archives Recovery ===")
    for arg in args[1:]:
        try:
            print(f"Acessing file '{arg}'")
            temp = open(arg, "r")
            content = temp.read()
            print("---\n")
            print(content)
            print("\n---")
            temp.close()
            print(f"File '{arg}' closed.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file '{arg}': {e}", file=sys.stderr)
            return


if __name__ == "__main__":
    main()
