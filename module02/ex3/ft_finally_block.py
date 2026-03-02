"""Exercise 3: Finally Block - Always Clean Up."""


def water_plants(plant_list: list[str | None]) -> None:
    """Water each plant in the list, always closing the system after."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
        print("Watering completed successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Demonstrate normal and error watering scenarios."""
    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])

    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
