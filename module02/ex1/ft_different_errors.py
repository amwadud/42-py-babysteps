#!/usr/bin/env python3
"""Exercise 1: Demonstrates different Python
error types in a garden context."""


def garden_operations() -> None:
    """Show each error type, catch it, then demonstrate multi-catch."""
    print("Testing ValueError...")
    try:
        _ = int("not_a_number")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print()

    print("Testing ZeroDivisionError...")
    try:
        _ = 5 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print()

    print("Testing FileNotFoundError...")
    try:
        with open("missing.txt", "r") as f:
            _ = f.read()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print()

    print("Testing KeyError...")
    try:
        plant_data: dict[str, int] = {"tomato": 3}
        _ = plant_data["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print()

    print("Testing multiple errors together...")
    try:
        _ = int("abc")
    except (ValueError, ZeroDivisionError, KeyError) as e:
        print(f"Caught an error ({type(e).__name__}), but program continues!")
    print()

    print("All error types tested successfully!")


def test_error_types() -> None:
    """Print header and run garden_operations."""
    print("=== Garden Error Types Demo ===")
    print()
    garden_operations()


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
