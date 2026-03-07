#!/usr/bin/env python3
import sys
import math


def calc_dist(
    p1: tuple[float, float, float], p2: tuple[float, float, float]
) -> float:
    """Calculate Euclidean distance between two 3D points (tuples)."""
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2
    )


def parse_coords(coord_str: str) -> tuple[int, int, int]:
    """Parse a comma-separated string into a 3D tuple."""
    parts = coord_str.split(",")
    return (int(parts[0]), int(parts[1]), int(parts[2]))


def main() -> None:
    print("=== Game Coordinate System ===\n")

    # Basic Tuple Usage
    origin = (0, 0, 0)
    spawn = (10, 20, 5)
    print(f"Position created: {spawn}")
    print(
        f"Distance between {origin} and {spawn}: "
        + f"{calc_dist(origin, spawn):.2f}\n"
    )

    # Parsing coordinates using split()
    coord_input = "3,4,0"
    print(f'Parsing coordinates: "{coord_input}"')
    parsed_pos = parse_coords(coord_input)
    print(f"Parsed position: {parsed_pos}")
    dist_parsed = calc_dist(origin, parsed_pos)
    print(f"Distance between {origin} and {parsed_pos}: {dist_parsed}\n")

    # Handling invalid input gracefully
    invalid_input = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_input}"')
    try:
        _ = parse_coords(invalid_input)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")

    # Tuple Unpacking Magic
    print("Unpacking demonstration:")
    x, y, z = parsed_pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
