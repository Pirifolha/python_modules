#!/usr/bin/env python3

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    valid_ingredients: list[str] = dark_spell_allowed_ingredients()
    split_ingredients = ingredients.split(",")

    for ingredient in split_ingredients:
        if ingredient in valid_ingredients:
            return "VALID"
    return "INVALID"
