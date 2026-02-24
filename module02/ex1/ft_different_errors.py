#!/usr/bin/env python3


def garden_operations() -> None:
    print("=== Garden Error Types Demo ===")

    missingfile = "missing.txt"
    lst = {1, 2, 3, 4, 5}

    try:
        print("Testing ValueError...")
        _ = int("not_a_number")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
        print()

    try:
        print("Testing ZeroDivisionError...")
        _ = 753 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
        print()

    try:
        print("Testing FileNotFoundError...")
        _ = open(missingfile, "r")
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{missingfile}'")
        print()

    try:
        print("Testing KeyError...")
    except KeyError:
        print("Caught KeyError: Key not found in dictionary")
        print()


if __name__ == "__main__":
    garden_operations()
