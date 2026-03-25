#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
        if temp > 40:
            raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)")
        elif temp < 0:
            raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature is now {temp_str}°C!\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
        return 0
    return 0


def test_temperature_input() -> None:
    good: str = "25"
    print(f"Input data: '{good}'")
    if input_temperature(good) != 0:
        print("Crash")
        return

    bad: str = "abc"
    print(f"Input data: '{bad}'")
    if input_temperature(bad) != 0:
        print("Crash")
        return

    extreme_pos: str = "100"
    print(f"Input data: '{extreme_pos}'")
    if input_temperature(extreme_pos) != 0:
        print("Crash")
        return

    extreme_neg: str = "-50"
    print(f"Input data: '{extreme_neg}'")
    if input_temperature(extreme_neg) != 0:
        print("Crash")
        return

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
