#!/usr/bin/env python3


class Plant:
    """Blueprint for a plant with a name, height, and age."""

    plans_number = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new plant with the given name, height, and age."""
        self.name = name
        self.height = height
        self.age = age
        Plant.plans_number += 1
        print(f"Created plant: {self.get_info()}")

    def grow(self, cm: int = 1):
        """Add centimeters to the plant's height."""
        self.height += cm

    def grow_older(self, days: int = 1):
        """Add days to the plant's age."""
        self.age += days

    def show(self):
        """Print the plant's information to the console."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def get_info(self) -> str:
        """Get the plant's information as a string."""
        return f"{self.name} ({self.height}cm, {self.age} days)"


if __name__ == "__main__":
    p1 = Plant("Rose", 30, 25)
    p2 = Plant("Oak", 200, 365)
    p2 = Plant("Cactus", 5, 90)
    p3 = Plant("Sunflower", 80, 45)
    p4 = Plant("Fern", 15, 120)
    print(f"Total plants created: {Plant.plans_number}")
