#!/usr/bin/env python3


def healing_potion() -> str:
    from .elements import create_air, create_earth

    return (
        f"Healing potion brewed with '{create_air()}'"
        f" and '{create_earth()}'"
    )


def strength_potion() -> str:
    from elements import create_water, create_fire

    return (
        f"Strength potion brewed with '{create_fire()}'"
        f" and '{create_water()}'"
    )
