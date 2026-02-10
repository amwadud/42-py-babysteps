#!/usr/bin/env python3


class Plant:
    """
    Blueprint for a plant with a name, height, and age.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Construct a new plant with the given name, height, and age.
        """
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        """
        Print the plant's information to the console.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    for p in plants:
        p.show()
