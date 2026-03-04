#!/usr/bin/env python3

# Authorized: import sys, sys.argv, import math, tuple(),
# int(), float(), print(), split(), try/except, math.sqrt()

from math import sqrt


class CoordinatesError(Exception):
    pass


class Position:
    x: int
    y: int
    z: int

    def __init__(
        self, coords: tuple[int, int, int], creation_str: str = ""
    ) -> None:
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]
        print(creation_str, end="")

    def set(self, coords: tuple[int, int, int]) -> None:
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]

    def get(self) -> tuple[int, int, int]:
        return (self.x, self.y, self.z)

    def __str__(self) -> str:
        return str((self.x, self.y, self.z))

    # def pars(self) -> str:
    #     return f'"{self.x},{self.y},{self.z}"'

    def dist(self, coords: tuple[int, int, int]) -> float:
        return sqrt(
            (coords[0] - self.x) ** 2
            + (coords[1] - self.y) ** 2
            + (coords[2] - self.z) ** 2
        )


def create_pos(x: int = 0, y: int = 0, z: int = 0) -> Position:
    p = Position((x, y, z))
    print("Position created: ")
    return p


def game_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    try:
        print()
        _ = Position((10, 20, 5), "Position created: (10, 20, 5)\n")
        print(
            "Distance between (0, 0, 0) and (10, 20, 5): "
            + f"{Position((0, 0, 0)).dist((10, 20, 5))}"
        )
        print()
        print('Parsing coordinates: "3,4,0"')
        print(f"Parsed position: {Position((3, 4, 0))}")
        print(
            f"Distance between {Position((0, 0, 0))} and "
            + f"{Position((3, 4, 0))}: {Position((3, 4, 0)).dist((0, 0, 0))}"
        )
        print()
        print('Parsing invalid coordinates: "abc,def,ghi"')
        _ = Position((int("w"), int("r"), int("g")))
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(
            f"Error details - Type: {type(error).__name__}, Args: {error.args}"
        )
    print()
    print("Unpacking demonstration:")
    position = (3, 4, 0)
    x, y, z = position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main() -> None:
    game_coordinate_system()


if __name__ == "__main__":
    main()
