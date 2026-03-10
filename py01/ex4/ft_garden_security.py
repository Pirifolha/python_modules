#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name) -> None:
        self.name = name
        self.__height = 0
        self.__age = 0

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def set_age(self, age) -> None:
        if age > 0:
            self.__age = age
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def set_height(self, height) -> None:
        if height > 0:
            self.__height = height
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")


rose = SecurePlant("Rose")
rose.set_age(-81)
rose.set_height(0)


def main():
    if rose.get_age() > 0 and rose.get_height() > 0:
        print(f"Plant created: {rose.name}")
        print(f"Height updated: {rose.get_height()}cm [OK]")
        print(f"Age updated: {rose.get_age()} days [OK]")
        print(f"Current plant: {rose.name} "
              f"({rose.get_height()}cm, {rose.get_age()} days)")


if __name__ == "__main__":
    main()
