#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
    except ValueError as e:
        print(f"Caught {input_temperature.__name__} error: {e}")
        return 0
    print(f"Temperature {temp}°C is perfect for plants!\n")
    return 0


def test_temperature() -> None:
    good: str = "25"
    print(f"Testing temperature: {good}")
    if input_temperature(good) != 0:
        print("Crash")
        return

    bad: str = "abc"
    print(f"Testing temperature: {bad}")
    if input_temperature(bad) != 0:
        print("Crash")
        return

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
