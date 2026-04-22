#!/usr/bin/env python3
from .elements import create_air, create_earth
from elements import create_water, create_fire


def healing_potion() -> str:

    return (
        f"Healing potion brewed with '{create_air()}'"
        f" and '{create_earth()}'"
    )


def strength_potion() -> str:

    return (
        f"Strength potion brewed with '{create_fire()}'"
        f" and '{create_water()}'"
    )
