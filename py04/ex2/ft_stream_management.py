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
            print(f"Acessing file '{arg}'")
            temp: IO[str]
            temp = open(arg, "r+")
            content = temp.read()
            temp.seek(0)
            temp.write("---\n\n" + content)
            temp.close()
            temp = open(arg, "a")
            temp.write("\n\n---")
            temp.close()
            temp = open(arg, "r")
            print(temp.read())
            temp.close()
            print(f"File '{arg}' closed.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file '{arg}': {e}", file=sys.stderr)
            return
        print("Transforming data:")
        file: IO[str]
        lines = []
        new_lines = []
        file = open(arg, "r")
        for line in file:
            lines.append(line)
        file.close()
        file = open(arg, "r")
        for line in lines:
            if line[0] == "\n" or line[0] == "-":
                print(line.rstrip("\n"))
            else:
                new_lines.append(line.rstrip("\n") + "#\n")
                print(line.rstrip("\n") + "#")
        file.close()
        print("Enter new file name (or empty): ", end="", flush=True)
        new_name: str = sys.stdin.readline()
        if new_name.strip():
            try:
                open(new_name, "x")
            except (FileNotFoundError, PermissionError) as e:
                print(f"Error opening file '{arg}': {e}", file=sys.stderr)
                return print("Not saving data.")
            file = open(new_name, "w")
            for line in new_lines:
                file.write(line)
            file.close()
            print(
                f"Saving data to '{new_name.rstrip('\n')}'\n"
                f"Data saved to '{new_name.rstrip('\n')}'"
            )
        else:
            print("Not saving data.")


if __name__ == "__main__":
    main()
