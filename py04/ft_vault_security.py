def secure_archive(
    filename: str,
    action: str = "read",
    content: str = "",
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as f:
                txt = f.read()
            try:
                txt1 = f.read()
                print(txt1)
            except Exception as e:
                print(f"{e}\n\n\n")
                return (True, txt)
        else:
            with open(filename, "w") as f:
                f.write(content)
                return (True, "Content successfully written to file")
    except (OSError, UnicodeDecodeError) as e:
        return (False, str(e))


if __name__ == "__main__":
    secure_archive("ancient_fragment.txt", "write", "[FRAGMENT 001]")
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a non existent file:")
    print(secure_archive("what/the/helly"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "write", result[1]))
