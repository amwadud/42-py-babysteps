#!/usr/bin/env python3
"""Module for simulating plant growth and aging."""


class Plant:
    """Blueprint for a plant with a name, height, and age."""

    def __init__(self, name: str, height: int, longevity: int) -> None:
        """Construct a new plant with attributes."""
        self.name = name
        self.height = height
        self.longevity = longevity

    def grow(self, cm: int = 1) -> None:
        """Add centimeters to the plant's height."""
        self.height += cm

    def age(self, days: int = 1) -> None:
        """Add days to the plant's age."""
        self.longevity += days

    def get_info(self) -> str:
        """Return the plant's current status as a string."""
        return f"{self.name}: {self.height}cm, {self.longevity} days old"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    cactus = Plant("Cactus", 15, 120)

    rose_start_h = rose.height

    print("=== Day 1 ===")
    print(rose.get_info())
    print(cactus.get_info())

    rose.grow(6)
    rose.age(6)

    cactus.grow()
    cactus.age(6)

    print("=== Day 7 ===")
    print(rose.get_info())
    print(cactus.get_info())
    print(f"Growth this week: +{rose.height - rose_start_h}cm")
