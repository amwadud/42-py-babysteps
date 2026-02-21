#!/usr/bin/env python3
"""Module for Exercise 5: Specialized Plant Types (Inheritance)."""


class Plant:
    """Base blueprint for all plant types."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize common plant attributes."""
        self.name = name
        self.height = height
        self.age = age

    def get_base_info(self) -> str:
        """Helper to get common info string."""
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    """Subclass representing a flowering plant."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Call parent setup and add color."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Print a blooming message."""
        print(f"{self.name} is blooming beautifully!")

    def show_info(self) -> None:
        """Match the output format: Name (Flower): ...."""
        print(
            f"{self.name} (Flower): {self.height}cm, "
            f"{self.age} days, {self.color} color"
        )


class Tree(Plant):
    """Subclass representing a tree."""

    def __init__(self, name: str, height: int, age: int, diameter: int) -> None:
        """Call parent setup and add trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter = diameter

    def produce_shade(self) -> None:
        """Simulate shade. Formula: diameter * 1.56 (78 for 50)."""
        shade_area = int(self.trunk_diameter * 1.56)
        print(f"{self.name} provides {shade_area} square meters of shade")

    def show_info(self) -> None:
        """Match the output format: Name (Tree): ...."""
        print(
            f"{self.name} (Tree): {self.height}cm, "
            f"{self.age} days, {self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    """Subclass representing a vegetable plant."""

    def __init__(
        self, name: str, height: int, age: int, season: str, nutrition: str
    ) -> None:
        """Initialize with parent and specific vegetable traits."""
        super().__init__(name, height, age)
        self.harvest_season = season
        self.nutritional_value = nutrition

    def show_nutrition(self) -> None:
        """Display nutrition info."""
        print(f"{self.name} is rich in {self.nutritional_value}")

    def show_info(self) -> None:
        """Match the output format: Name (Vegetable): ...."""
        print(
            f"{self.name} (Vegetable): {self.height}cm, "
            f"{self.age} days, {self.harvest_season} harvest"
        )


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")

    rose.show_info()
    rose.bloom()
    print()

    oak.show_info()
    oak.produce_shade()
    print()

    tomato.show_info()
    tomato.show_nutrition()
