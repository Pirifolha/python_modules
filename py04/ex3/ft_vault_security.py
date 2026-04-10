#!/usr/bin/env python3


def secure_archive(file: str, action: str, content: str) -> tuple[bool, str]:
    try:
        with open(file, action) as temp:
            if action == "w":
                temp.write(content)
            elif action == "r":
                return True, temp.read()
    except (FileNotFoundError, PermissionError) as e:
        return False, f"Error opening file '{file}': {e}"
    return True, "Content successfully written to file"


if __name__ == "__main__":
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("", "r", "adssdlaldsldldad\nsaddsdssd"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "r", "asdasd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("test.txt", "r", "asadasdds"))

    print("\nUsing'secure_archive' to write previous content to a new file:")
    print(secure_archive("test.txt", "w", "jhello"))