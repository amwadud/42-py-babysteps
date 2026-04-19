#!/usr/bin/env python3
"""Module for Exercise 3: Plant Factory."""


class Plant:
    """
    Blueprint for a plant.
    Tracks total instances created using a class attribute.
    """

    # Normally speaking, I'll need something to show that this variable is a
    # class level variable, but since the instructions forbids other
    # python features.attribute, I'll just use it as is.
    total_count: int = 0

    name: str
    height: int
    age: int

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize the plant and update the factory counter.
        Displays the creation message immediately.
        """
        self.name = name
        self.height = height
        self.age = age

        Plant.total_count += 1

        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    garden_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    for name, height, age in garden_data:
        _ = Plant(name, height, age)

    print(f"Total plants created: {Plant.total_count}")
