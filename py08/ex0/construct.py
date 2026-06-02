#!/usr/bin/env python3

import site
import sys
import os


def neg_venv() -> None:
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(
        f"Current Python: {sys.executable}\n"
        f"Virtual Enviroment: None detected\n"
        "WARNING: You're in the global environment!\n"
        "The machines can see everything you install.\n"
        "To enter the cosntruct, run:\n"
        "python -m venv matrix_env\n"
        "source matrix_env/bin/activate # On Unix\n"
        r"matrix_env\Scripts\activate # On Windows"
    )
    print("\nThen run this program again")


def pos_venv() -> None:
    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(
        f"Current Python: {sys.executable}\n"
        f"Virtual Enviroment: {os.path.basename(sys.prefix)}\n"
        f"Environment Path: {sys.prefix}\n"
    )
    print(
        "SUCCESS: You're in an isolated environment!\n"
        "Safe to install packages without affecting\n"
        "the global system.\n"
    )
    print("Package installation path:\n" f"{site.getsitepackages()[0]}")


def test() -> None:
    if (
        hasattr(sys, "real_prefix")
        or (hasattr(sys, "base_prefix"))
        and sys.prefix != sys.base_prefix
    ):
        pos_venv()
    else:
        neg_venv()


if __name__ == "__main__":
    test()
