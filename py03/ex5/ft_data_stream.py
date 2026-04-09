#!/usr/bin/env python3

import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    names: list = ["Alice", "Bob", "Charlie", "Dylan"]
    actions: list = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use",
    ]

    while True:
        name = random.choice(names)
        action = random.choice(actions)
        event = (name, action)
        yield event


def main() -> None:
    gen = gen_event()
    for i in range(1000):
        name, action = next(gen)
        print(f"Event {i}: Player {name} did action {action}")
    events: list = []
    for i in range(10):
        events.append(next(gen))
    print(f"Built list of 10 events: {events}")
    consume = consume_event(events)
    for i in range(len(events)):
        n = next(consume)
        print(f"\nGot event from list: {n}")
        print(f"Remaining in list: {events}")


def consume_event(
    events: list[tuple],
) -> Generator[tuple[str, str], None, None]:
    for i in range(len(events)):
        event = random.choice(events)
        events.remove(event)
        yield event


if __name__ == "__main__":
    main()
