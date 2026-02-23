#!/usr/bin/env python3
"""Module for Exercise 3: Plant Factory."""


class Plant:
    """
    Blueprint for a plant.
    Tracks total instances created using a class attribute.
    """

    # Class attribute: Shared by the whole factory
    total_count = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize the plant and update the factory counter.
        Displays the creation message immediately.
        """
        self.name = name
        self.height = height
        self.age = age

        # Increment the shared factory counter
        Plant.total_count += 1

        # Display in the exact format required by the example
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    # Streamlining: Store data in a list to create many plants efficiently
    garden_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    # Create all plants using a loop
    for name, height, age in garden_data:
        Plant(name, height, age)

    # Final summary using the class attribute
    print(f"Total plants created: {Plant.total_count}")
