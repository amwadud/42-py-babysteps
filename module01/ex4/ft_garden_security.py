#!/bin/usr/env python3


class SecurePlant:
    """
    Secure version of the Plant class with private attributes and validation.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """Cosntruct a new plant with the given name, height, and age."""
        self.__name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.__name}")

    def show(self):
        """Print the plant's information to the console."""
        print(f"{self.__name}: {self.__height}cm, {self.__age} days old")

    def get_info(self) -> str:
        """Get the plant's information as a string."""
        return f"{self.__name}: {self.__height}cm, {self.__age} days old"

    def set_height(self, height: int):
        """
        Set the plant's height with validation to prevent negative values.
        """
        if height < 0:
            print(
                f"Invalid operation attempted: height {height}cm [REJECTED]\n"
                "Security: Negative height rejected\n\n"
                f"Current plant: {self.__name} "
                f"({self.__height}cm, {self.__age} days) "
            )
            return
        self.__height = height
        print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int):
        """Set the plant's age with validation to prevent negative values."""
        if age < 0:
            print("Age cannot be negative.")
            return
        self.__age = age
        print(f"Age updated: {age} days [OK]")

    def get_age(self) -> int:
        """Get the plant's age."""
        return self.__age

    def get_height(self) -> int:
        """Get the plant's height"""
        return self.__height


if __name__ == "__main__":
    print("=== Garden Security System === ")
    p1 = SecurePlant("Rose", 30, 15)
    p1.show()
    p1.set_height(35)
    p1.set_age(20)
    p1.show()
    p1.set_height(-5)  # Attempt to set invalid height
