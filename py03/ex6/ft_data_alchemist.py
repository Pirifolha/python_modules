#!/usr/bin/env python3

import random


def main() -> None:
    names: list = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]

    cap_names: list = [x.capitalize() for x in names]
    only_cap: list = [name for name in names if name[0].isupper()]
    dic_names: dict = {n: random.randrange(0, 1000) for n in cap_names}
    scores: set = set(dic_names.values())
    average = round(sum(scores) / len(scores))
    dic_keys: dict = {
        key: dic_names[key]
        for key in dic_names
        if dic_names[key] > average
    }

    print(f"Initial list of players: {names}\n")
    print(f"New list with all names capitalized: {cap_names}\n")
    print(f"New list of capitalized names only: {only_cap}\n")
    print(f"Score average is: {average}\n")
    print(f"High scores: {dic_keys}\n")


if __name__ == "__main__":
    main()
