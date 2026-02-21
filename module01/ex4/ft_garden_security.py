#!/usr/bin/env python3
"""Module for the Garden Security System: Exercise 4."""


class SecurePlant:
    """
    Secure version of the Plant class with private attributes and validation.
    Demonstrates the concept of Encapsulation.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Construct a new plant.
        Calls setters to ensure data integrity during initialization.
        """
        self.__name = name
        self.__height = 0
        self.__age = 0

        print(f"Plant created: {self.__name}")
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        """Return the encapsulated height."""
        return self.__height

    def get_age(self) -> int:
        """Return the encapsulated age."""
        return self.__age

    def set_height(self, value: int) -> None:
        """
        Set the plant's height with validation.
        Rejects negative values to maintain data integrity.
        """
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int) -> None:
        """
        Set the plant's age with validation.
        Rejects negative values to maintain data integrity.
        """
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = value
            print(f"Age updated: {value} days [OK]")

    def get_info(self) -> str:
        """Return the official status string for the plant."""
        return f"{self.__name} ({self.__height}cm, {self.__age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p1 = SecurePlant("Rose", 25, 30)
    print()
    p1.set_height(-5)
    print()
    print("Current plant:", p1.get_info())
