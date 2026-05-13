#!/usr/bin/env python3

import sys


class ParameterError(Exception):
    def __init__(self, message="Invalid parameter:"):
        super().__init__(message)


class DuplicateError(Exception):
    def __init__(self, message="Invalid parameter:"):
        super().__init__(message)


def main() -> None:
    inventory: dict = {}
    keys: list = ['sword', 'potion', 'shield', 'armor', 'helmet']
    for arg in sys.argv[1:]:
        try:
            temp = arg.split(':')
            if len(temp) != 2:
                raise ParameterError()
            key, value = temp
            if key not in keys:
                raise ParameterError()
            elif key in inventory:
                raise DuplicateError()
            try:
                inventory[key] = int(value)
            except ValueError as e:
                print(f"Quantity error for '{key}' {e}")
        except ParameterError:
            print(f"Error - invalid parameter {temp[0]}")
        except DuplicateError:
            print(f"Redundant item {key} - discarding")
    print(f"Got inventory: {inventory}")
    keys_inv = list(inventory.keys())
    values_inv = list(inventory.values())
    print(f"Item list: {keys_inv}")
    print(f"Total quantity of the {len(keys_inv)} "
          f"items: {sum(values_inv)}")
    for key in inventory:
        total = sum(values_inv)
        v = inventory[key]
        percentage = round(v / total * 100)
        print(f"Item {key} represents: {percentage}%")
    max_value: int = 0
    max_name: str = ""
    for n in inventory:
        t_int: int = inventory[n]
        if t_int > max_value:
            max_value = t_int
            max_name = n
    if len(inventory) > 0:
        print(f"Item most abundant: {max_name} with quantity {max_value}")
    else:
        print("Item most abundant: None")
    min_value: int = max_value
    min_name: str = ""
    for i in inventory:
        tmp_int: int = inventory[i]
        if tmp_int < min_value:
            min_value = tmp_int
            min_name = i
        else:
            min_name = i
    if len(inventory) > 0:
        print(f"Item least abundant: {min_name} with quantity {min_value}")
    else:
        print("Item least abundant: None")
    inventory.update({"magic_item": 2})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
