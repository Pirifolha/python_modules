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
            with open(arg, "a") as temp:
                temp.write("\n\n---")
                temp.close()
                temp = open(arg, "r")
                print(temp.read())
                print(f"File '{arg}' closed.")
        except FileNotFoundError as e:
            print(f"Error opening file '{arg}': {e}")
            return
        except PermissionError as e:
            print(f"Error opening file '{arg}': {e}")
            return
        print("Transforming data:")
        file: IO[str]
        lines = []
        new_lines = []
        with open(arg, "r") as file:
            for line in file:
                lines.append(line)
        with open(arg, "r") as file:
            for line in lines:
                if line[0] == "\n" or line[0] == "-":
                    print(line.rstrip("\n"))
                else:
                    new_lines.append(line.rstrip("\n") + "#\n")
                    print(line.rstrip("\n") + "#")
        new_name: str = input("Enter new file name (or empty): ")
        if len(new_name) > 0:
            open(new_name, "x")
            with open(new_name, "w") as file:
                for line in new_lines:
                    file.write(line)
            print(
                f"Saving data to '{new_name}'\n" f"Data saved to '{new_name}'"
            )
        else:
            print("Not saving data.")


if __name__ == "__main__":
    main()
