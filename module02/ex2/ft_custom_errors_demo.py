#!/usr/bin/env python3

# === Custom exception classes ===


class GardenError(Exception):
    """Base class for all garden-related errors."""

    def __init__(self, message: str):
        super().__init__(message)


class PlantError(GardenError):
    """Error for plant-related problems."""

    def __init__(self, message: str = "A plant problem occurred"):
        super().__init__(message)


class WaterError(GardenError):
    """Error for watering-related problems."""

    def __init__(self, message: str = "A watering problem occurred"):
        super().__init__(message)


# === Functions that raise custom errors ===


def check_plant_health(plant: str):
    """Simulate a plant problem."""
    if plant.lower() == "tomato":
        raise PlantError("The tomato plant is wilting!")


def check_water_supply(amount: int):
    """Simulate a watering problem."""
    if amount < 5:
        raise WaterError("Not enough water in the tank!")


# === Demo: catching specific errors ===


def garden_demo():
    print("=== Custom Garden Errors Demo ===\n")

    # 1️⃣ Catch specific errors individually
    try:
        print("Testing PlantError...")
        check_plant_health("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        print("Testing WaterError...")
        check_water_supply(3)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")

    # 2️⃣ Catch all garden-related errors via the base class
    for func, args in [
        (check_plant_health, ("tomato",)),
        (check_water_supply, (2,)),
    ]:
        try:
            func(*args)
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    garden_demo()
