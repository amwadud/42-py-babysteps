#!/usr/bin/env python3
"""Module for a secure plant management system with data validation."""


class SecurePlant:
    """
    A plant class that protects its data from invalid values.
    Uses Encapsulation to ensure data integrity.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant and set initial values through secure setters."""
        self._name = name
        self._height = 0
        self._age = 0

        print(f"Plant created: {self._name}")
        self.set_height(height)
        self.set_age(age)

    # --- Getters
    def get_height(self) -> int:
        """Return the current height."""
        return self._height

    def get_age(self) -> int:
        """Return the current age."""
        return self._age

    # --- Setters
    def set_height(self, value: int) -> None:
        """Validate and set plant height."""
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int) -> None:
        """Validate and set plant age."""
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days [OK]")

    def get_info(self) -> str:
        """Return a string representation of the plant."""
        return (
            f"Current plant: {self._name} ({self._height}cm, {self._age} days)"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")

    # Create a plant
    rose = SecurePlant("Rose", 25, 30)
    print("")

    # Attempt an invalid operation (Negative height)
    rose.set_height(-5)

    # Show final status
    print(rose.get_info())
