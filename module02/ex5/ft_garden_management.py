#!/usr/bin/env python3
"""Exercise 5: Garden Management System."""


class GardenError(Exception):
    """Base error for garden problems."""

    pass


class PlantError(GardenError):
    """Error for plant-specific problems."""

    pass


class WaterError(GardenError):
    """Error for watering problems."""

    pass


class GardenManager:
    """Manages plants with full error handling."""

    plants: dict[str, dict[str, int]]

    def __init__(self) -> None:
        """Initialize the garden with an empty plant list."""
        self.plants = {}

    def add_plant(
        self, name: str, water_level: int = 5, sunlight_hours: int = 8
    ) -> None:
        """Add a plant to the garden."""
        if not name:
            raise PlantError("Plant name cannot be empty!")
        self.plants[name] = {"water": water_level, "sun": sunlight_hours}
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        """Water all plants, always closing the system after."""
        print("Opening watering system")
        try:
            for name in self.plants:
                print(f"Watering {name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, name: str) -> None:
        """Check health of a specific plant."""
        if name not in self.plants:
            raise PlantError(f"Plant '{name}' not found in garden!")
        plant = self.plants[name]
        if plant["water"] > 10:
            raise WaterError(
                f"Water level {plant['water']} is too high (max 10)"
            )
        print(
            f"{name}: healthy (water: {plant['water']}, sun: {plant['sun']})"
        )


def main() -> None:
    """Run the garden management system demo."""
    print("=== Garden Management System ===")
    print()
    manager = GardenManager()

    print("Adding plants to garden...")
    print()
    for args in [("tomato", 5, 8), ("lettuce", 3, 6), ("", 5, 8)]:
        try:
            manager.add_plant(*args)
        except PlantError as e:
            print(f"Error adding plant: {e}")
    print()

    print("Watering plants...")
    manager.water_plants()
    print()

    print("Checking plant health...")
    manager.plants["lettuce"]["water"] = 15
    for name in ["tomato", "lettuce"]:
        try:
            manager.check_health(name)
        except (PlantError, WaterError) as e:
            print(f"Error checking {name}: {e}")

    print("Testing error recovery...")
    print()
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    print()

    print("Garden management system test complete!")


if __name__ == "__main__":
    main()
