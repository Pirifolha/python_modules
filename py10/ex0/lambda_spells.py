#!/usr/bin/env python3


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_artifacts: list[dict] = sorted(
        artifacts, key=lambda x: x["power"], reverse=True
    )
    return sorted_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered_mages = list(filter(lambda x: x["power"] > min_power, mages))
    return filtered_mages


def spell_transformer(spells: list[str]) -> list[str]:
    transformed_spells = list(map(lambda x: "* " + x + " *", spells))
    return transformed_spells


def mage_stats(mages: list[dict]) -> dict:
    maximum: dict = max(mages, key=lambda x: x["power"])
    minimum: dict = min(mages, key=lambda x: x["power"])
    average: float = sum(map(lambda x: x["power"], mages)) / len(mages)
    ret_dict = {
        "max_power": maximum["power"],
        "min_power": minimum["power"],
        "avg_power": average,
    }
    return ret_dict


artifacts = [
    {"name": "Crystal Orb", "power": 85, "type": "weapon"},
    {"name": "Lightning Rod", "power": 110, "type": "accessory"},
    {"name": "Earth Shield", "power": 120, "type": "armor"},
    {"name": "Crystal Orb", "power": 89, "type": "armor"},
]

mages = [
    {"name": "Jordan", "power": 95, "element": "ice"},
    {"name": "Zara", "power": 82, "element": "ice"},
    {"name": "Alex", "power": 70, "element": "wind"},
    {"name": "Storm", "power": 65, "element": "light"},
    {"name": "Storm", "power": 66, "element": "water"},
]
spells = ["blizzard", "fireball", "heal", "shield"]


def main() -> None:
    print("\nTesting artifact sorter...")

    sorted_artifacts = artifact_sorter(artifacts)

    print(
        f"{sorted_artifacts[-1]['name']} ({sorted_artifacts[-1]['power']} "
        f"power) comes after "
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power)"
        "\n"
    )

    print("Testing spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))


main()
