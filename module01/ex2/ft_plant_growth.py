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

    def grow(self, cm: int = 1):
        """
        Add centimeters to the plant's height.
        """
        self.height += cm

    def grow_older(self, days: int = 1):
        """
        Add days to the plant's age.
        """
        self.age += days

    def show(self):
        """
        Print the plant's information to the console.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def get_info(self) -> str:
        """
        Get the plant's information as a string.
        """
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    p1 = Plant("Rose", 30, 15)
    prev_height = p1.height
    print("== Day 1 ==")
    p1.show()
    p1.grow(5)
    p1.grow_older(5)
    print("== Day 7 ==")
    p1.show()
    print(f"Growth this week: +{p1.height - prev_height}")
