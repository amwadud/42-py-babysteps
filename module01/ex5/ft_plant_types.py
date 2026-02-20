#!/usr/bin/env python3


class Plant:
    """
    Blueprint for a plant with a name, height, and age.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a new plant with the given name, height, and age.
        """
        self.name = name
        self.height = height
        self.age = age


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
        print(f"{self.name} is blooming beautifuly!")


class Tree(Plant):
    """
    Some description.
    """

    def __init__(
        self, name: str, height: int, age: int, trunk_diameter: int
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        Simulate the tree providing shade.
        """
        print("Oak provides {self.trunk_diameter} square meters of shade")


class Vegetable(Plant):
    """
    Some description.
    """

    def __iniit__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: int,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
