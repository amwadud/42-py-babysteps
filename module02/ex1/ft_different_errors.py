#!/usr/bin/env python3


def garden_operations() -> None:
    """Functions that demonstrate various error types in a garden context."""
    print("=== Garden Error Types Demo ===\n")

    missing_file: str = "missing.txt"
    plant_names: dict[str, int] = {
        "plant1": 10,
        "plant2": 20,
        "plant3": 30,
    }
    missing_plant: str = "missing\\_plant"
    found_error: bool = False

    try:
        print("Testing ValueError...")
        _ = int("not_a_number")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
        print()
        found_error = True

    try:
        print("Testing ZeroDivisionError...")
        _ = 753 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
        print()
        found_error = True

    try:
        print("Testing FileNotFoundError...")
        _ = open(missing_file, "r")
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{missing_file}'")
        print()
        found_error = True

    try:
        print("Testing KeyError...")
        _ = plant_names[missing_plant]
    except KeyError:
        print(f"Caught KeyError: '{missing_plant}'")
        print()
        found_error = True

    print("Testing multiple errors together...")
    if found_error:
        print("Caught an error, but the program continues!")
    print("All error types tested successfully!")


if __name__ == "__main__":
    garden_operations()
