#!/usr/bin/env python3
"""Solution for: Exercise 2 - Making Your Own Error Types"""


class GardenError(Exception):
    """Base class for garden-related errors."""

    pass


class PlantError(GardenError):
    """Raised when there is a plant-related issue."""

    pass


class WaterError(GardenError):
    """Raised when there is a water-related issue."""

    pass


def test_plant_error():
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")


def test_water_error():
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")


def test_catch_all():
    print("Testing catching all garden errors...")
    errors = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!"),
    ]

    for err in errors:
        try:
            raise err
        except GardenError as e:
            print(f"Caught a garden error: {e}")


def main():
    print("=== Custom Garden Errors Demo ===\n")
    test_plant_error()
    test_water_error()
    test_catch_all()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
