#!/usr/bin/env python3

from collections.abc import Callable


def mage_counter() -> Callable:
    x = 0

    def counter() -> int:
        nonlocal x
        x += 1
        return x

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def power(add: int) -> int:
        nonlocal total_power
        total_power += add
        return total_power

    return power


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchanted_item(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchanted_item


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: int) -> None:
        memory[key] = value

    def recall(key) -> int | str:
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter = mage_counter()
    counter2 = mage_counter()
    for _ in range(3):
        print(f"counter call {_+1}:", counter())

    for _ in range(2):
        print(f"counter2 call {_+1}:", counter2())

    print("\nTesting spell accumulator...")
    power = spell_accumulator(5)
    print("Base 5, add 10:", power(10))
    print("Base 5, add 20:", power(20))

    print("\nTesting enchantment_factory...")
    flame = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flame("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)

    print("Recall 'secret':", vault["recall"]("secret"))
    print("Recall 'unknown':", vault["recall"]("unknown"))
