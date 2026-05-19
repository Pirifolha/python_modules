#!/usr/bin/env python3

import sys


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_stream_management.py <file>")
        sys.exit()
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        f = open(sys.argv[1])
    except (OSError, UnicodeDecodeError) as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")
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
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        filename = sys.stdin.readline().rstrip("\n")
        if not filename:
            print("Not saving data.")
        else:
            print(f"Saving data to '{filename}'")
            try:
                file = open(filename, "w")
                file.write(content)
                file.close()
                print(f"Data saved in file '{filename}'.")
            except (OSError, UnicodeDecodeError) as e:
                sys.stderr.write(
                    f"[STDERR] Error opening " f"file '{sys.argv[1]}': {e}\n"
                )
                print("Data not saved.")


if __name__ == "__main__":
    main()
