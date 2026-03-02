#!/usr/bin/env python3
"""
Garden Plant Health Checker 🌱

Simple validation logic demonstrating:
- Type hints
- Docstrings (PEP 257 style)
- Defensive programming (input validation)
- Clear error messages
"""


def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int,
) -> None:
    """
    Validate plant health conditions and print the result.

    Parameters
    ----------
    plant_name : str
        Name of the plant. Must be a non-empty string.
    water_level : int
        Water level between 1 and 10 (inclusive).
    sunlight_hours : int
        Sunlight exposure between 2 and 12 hours (inclusive).

    Returns
    -------
    None
        Prints validation result instead of returning a value.

    Raises
    ------
    ValueError
        If any validation rule is violated.
    """

    try:
        # --- Plant name validation ---
        if not plant_name.strip():
            raise ValueError("Plant name cannot be empty.")

        # --- Water validation ---
        if not 1 <= water_level <= 10:
            raise ValueError(
                f"Water level {water_level} is out of range (1–10)."
            )

        # --- Sunlight validation ---
        if not 2 <= sunlight_hours <= 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is out of range (2–12)."
            )

    except ValueError as error:
        print(f"[ERROR] {error}")
        return None

    print(f"[OK] Plant '{plant_name}' is healthy. 🌿")


def test_plant_checks() -> None:
    """
    Run manual test cases for plant validation logic.
    """

    print("=== Garden Plant Health Checker ===\n")

    print("Testing valid input...")
    check_plant_health("tomato", 5, 8)
    print()

    print("Testing empty plant name...")
    check_plant_health("", 5, 8)
    print()

    print("Testing invalid water level...")
    check_plant_health("tomato", 100, 8)
    print()

    print("Testing invalid sunlight hours...")
    check_plant_health("tomato", 5, 0)
    print()

    print("All tests completed.")


if __name__ == "__main__":
    test_plant_checks()
