#!/usr/bin/env python3


def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    valid_ingredients: list[str] = light_spell_allowed_ingredients()
    split_ingredients = ingredients.split(",")

    for ingredient in split_ingredients:
        if ingredient.strip() in valid_ingredients:
            return "VALID"
    return "INVALID"
