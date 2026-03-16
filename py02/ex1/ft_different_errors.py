#!/usr/bin/env python3


def garden_operation() -> None:
    print("Testing ValueError...")
    try:
        int("Abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    print("Testing ZeroDivisionError...")
    try:
        4 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    print("Testing FileNotFoundError...")
    try:
        f = open("missing.txt", "r")
        f.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    print("Testing KeyError...")
    try:
        temp: dict[str, str] = {"name": "Miguel", "school": "42"}
        print(temp["plant"])
    except KeyError:
        print("Caught KeyError: 'missing/_plant'\n")
    print("Testing multiple errors together...")
    try:
        int("abc")
        3 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operation()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
