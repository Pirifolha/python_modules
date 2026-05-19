#!/usr/bin/env python3

import sys
from typing import IO


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        sys.exit(1)
    print("== Cyber Archives Recovery ===")
    try:
        print(f"Acessing file '{sys.argv[1]}'")
        f: IO[str] = open(sys.argv[1], "r+")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{sys.argv[1]}': {e}", file=sys.stderr)
    else:
        content = f.read()
        print("---")
        print()
        print(content)
        f.close()
        print("---")
        print(f"File '{sys.argv[1]}' closed.")
        print()
        print("Transform data:")
        print("---")
        print()
        content = content.replace("\n", "#\n")
        print(content)
        print("---")
        try:
            filename = input("Enter new file name (or empty): ")
        except EOFError:
            print("Not saving data.")
            sys.exit(1)
        if not filename:
            print("Not saving data.")
        else:
            print(f"Saving data to '{filename}'")
            try:
                file = open(filename, "w")
                file.write(content)
                file.close()
                print(f"Data saved in file '{filename}'.")
            except OSError as e:
                print(f"Error opening file '{filename}': {e}")
                print("Data not saved.")


if __name__ == "__main__":
    main()
