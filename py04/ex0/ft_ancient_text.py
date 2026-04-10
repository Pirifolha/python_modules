#!/usr/bin/env python3

import sys
from typing import IO


def main() -> None:
    args: list[str] = sys.argv
    if len(args) == 1:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("== Cyber Archives Recovery ===")
    for arg in args[1:]:
        try:
            print(f"Acessing file {arg}")
            temp: IO[str]
            with open(arg, "r+") as temp:
                content = temp.read()
                temp.seek(0)
                temp.write("---\n\n" + content)
            temp = open(arg, "a")
            temp.write("\n\n---")
            temp.close()
            temp = open(arg, "r")
            print(temp.read())
            temp.close()
            print(f"File {arg} closed.")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")


if __name__ == "__main__":
    main()
