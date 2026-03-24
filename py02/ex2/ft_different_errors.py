#!/usr/bin/env python3


def garden_operation(operation_number: int) -> None:

    try:
        if operation_number == 0:
            int("Abc")
        elif operation_number == 1:
            4 / 0
        elif operation_number == 2:
            f = open("missing.txt", "r")
            f.close()
        elif operation_number == 3:
            x = "hello" + 4
            print(x)
        else:
            print("Operation completed successfully\n")
            return
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    for i in range(5):
        print(f"Testing operation {i}...")
        garden_operation(i)
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
