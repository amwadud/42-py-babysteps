#!/usr/bin/env python3


class Plant:
    """
    Blueprint for a plant with a name, height, and age.
    """
    plans_number = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a new plant with the given name, height, and age.
        """
        self.name = name
        self.height = height
        self.age = age
        Plant.plans_number += 1


class Flower(Plant):
    """
    Class representing a flower, inheriting from Plant.
    It can have additional attributes or methods specific to flowers.
    """

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """
        Simulate the blooming of the flower.
        """
        print(f"{self.name} is blooming with {self.color} petals!")


class Tree(Plant):
    def __init__(
            self, name: str, height: int,
            age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        Simulate the tree providing shade.
        """
        print(f"{self.name} is providing shade "
              f"with its {self.height}cm height!")


class Vegetable(Plant):
    def __iniit__(
            self, name: str,
            height: int, age: int,
            harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":
    p1 = Plant("Rose", 30, 25)
    p2 = Plant("Oak", 200, 365)
    p2 = Plant("Cactus", 5, 90)
    p3 = Plant("Sunflower", 80, 45)
    p4 = Plant("Fern", 15, 120)
    print(f"Total plants created: {Plant.plans_number}")
