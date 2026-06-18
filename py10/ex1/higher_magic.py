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

    def amplified(*args, **kwargs) -> int:
        return base_spell(*args, **kwargs) * multiplier

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


def has_enough_power(target: str, power: int) -> bool:
    return power > 7


def damage_spell(power: int) -> int:
    return power


def main() -> None:
    power = 10
    combined = spell_combiner(heal, attack)
    mega_damage = power_amplifier(damage_spell, 3)
    original_result = damage_spell(power)
    amplified_result = mega_damage(power)
    cond = conditional_caster(has_enough_power, heal)
    seq = spell_sequence([heal, attack])

    print("\nTesting spell combiner...")
    print(f"Combined spell result: {', '.join(combined('Dragon', power))}")

    print("\nTesting power amplifier...")
    print(f"Original: {original_result}, Amplified: {amplified_result}")

    print("\nTesting conditional caster...")
    print(cond("Dragon", power))
    print(cond("Dragon", 3))

    print("\nTesting spell sequence...")
    print(seq("Dragon", power))


if __name__ == "__main__":
    main()
