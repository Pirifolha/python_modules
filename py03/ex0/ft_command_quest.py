#!/usr/bin/env python3

import sys


def main() -> None:
    program_name: str = sys.argv[0]
    args: int = len(sys.argv)
    if args == 1:
        print("No arguments received!")
    print(f"Program name: {program_name}")
    if args > 1:
        print(f"Arguments received: {args - 1}")
        for argument in sys.argv[1:]:
            n = 1
            print(f"Argument {sys.argv.index(argument)}: {argument}")
            n += 1
    print(f"Total arguments {args}\n")


if __name__ == "__main__":
    print("===Command quest===")
    main()
