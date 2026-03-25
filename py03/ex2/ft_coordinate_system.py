#!/usr/bin/env python3

import math


class LenError(Exception):
    def __init__(self, message="Invalid syntax"):
        super().__init__(message)


def get_player_pos() -> tuple:
    while True:
        try:
            temp_list = input(
                "Enter new coordinates as floats in format " "'x,y,z':"
            ).split(",")

            if len(temp_list) != 3:
                raise LenError

            coordinates = []
            for x in temp_list:
                temp = float(x)
                coordinates.append(temp)

            return tuple(coordinates)

        except LenError as e:
            print(f"{e}")
        except ValueError as e:
            print(f"Error on parameter '{x}': {e}")


def get_distance(coordinates1: tuple, coordinates2: tuple) -> float:
    center = math.sqrt(
        (coordinates2[0] - coordinates1[0]) ** 2
        + (coordinates2[1] - coordinates1[1]) ** 2
        + (coordinates2[2] - coordinates1[2]) ** 2
    )
    return round(center)


def main() -> None:
    print("Get a first set of coordinates")
    first_set: tuple = get_player_pos()
    zeros: tuple = (0, 0, 0)
    print(f"Got a first tuple: {first_set}")
    print(f"It includes: X={first_set[0]}, Y={first_set[1]}, Z={first_set[2]}")
    center_dis = get_distance(first_set, zeros)
    print(f"Distance to center: {center_dis}\n")

    print("Get a second set of coordinates")
    second_set: tuple = get_player_pos()
    sets_dis = get_distance(first_set, second_set)
    print(f"Distance between the 2 sets of coordinates: {sets_dis}")


if __name__ == "__main__":
    main()
