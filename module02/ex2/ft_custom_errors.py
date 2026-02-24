#!/usr/bin/env python3

class Plant:
    """Blueprint for plant, mainly for testing errors."""
    healthy: bool
    thirsty: bool
    def __init__(self, healthy: bool, thirsty: bool) -> None:
        pass

class GardenError(Exception):
    """Base class for all garden-related errors."""
    def __init__(self, message: str) -> None:
        super().__init__(message)

class PlantError(GardenError):
    """Error for plant-related problems."""
    def __init__(self, message: str = "A plant problem occurred"):
        super().__init__(message)

class WaterError(PlantError):
    """Error for watering-related problems."""
    def __init__(self, message: str = "A watering problem occurred"):
        super().__init__(message)

def garden_demo():
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        plant = "tomato"
        if (plant == "tomato")
            raise PlantError()
        if (plant == "tomato")
            raise WaterError()
        print("Testing WaterError...")
    except PlantError:
        print("Caught PlantError: The tomato plant is wilting!")
    except WaterError:
        print("Testing catching all garden errors...")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    garden_demo()
