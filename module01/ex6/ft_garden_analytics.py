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


class FloweringPlant(Plant):
    pass


class PrizeFlower(FloweringPlant):
    pass


class GardenManager:
    def __init__(self) -> None:
        pass

    def create_garden_network(self) -> None:
        pass

    def add(slef) -> None:
        pass

    def report(self) -> None:
        pass


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
