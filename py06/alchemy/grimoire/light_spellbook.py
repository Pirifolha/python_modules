#!/usr/bin/env python3

from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    if validate_ingredients(ingredients) == "INVALID":
        return f"Spell {spell_name} rejected - INVALID"
    else:
        return f"Spell recorded: {spell_name} {ingredients} - VALID"
