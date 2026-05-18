#!/usr/bin/env python3

from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def attack(target: str, power: int) -> str:
    return f"Attack takes {power} HP from {target}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    def combined(target, power) -> tuple:
        a = spell1(target, power)
        b = spell2(target, power)
        return (a, b)

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    def amplified(target, power) -> Callable:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    def conditioned(target, power) -> Callable | str:
        if condition(target, power) is True:
            return spell(target, power)
        else:
            return "Spell fizzled"

    return conditioned


def spell_sequence(spells: list[Callable]) -> Callable:

    def call_spell(target, power) -> list[Callable]:
        calls = []
        for x in spells:
            if callable(x):
                calls.append(x(target, power))
        return calls

    return call_spell


def test(target, power):
    if power > 7:
        return True
    else:
        return False


def main() -> None:
    power = 30
    combined = spell_combiner(heal, attack)
    # mega_heal = power_amplifier(heal, power)
    # cond = conditional_caster(test, heal)
    # seq = spell_sequence([heal, attack])

    print("\nTesting spell combiner...")
    print(f"Combined spell result: {', '. join(combined("Dragon", 30))}")

    print("\nTesting power amplifier...")
    print(f"Original:{power}, Amplified: {power * 3}")


if __name__ == "__main__":
    main()
