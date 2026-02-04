#!/usr/bin/env python3


class plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plants = [
        plant("Rose", 25, 30),
        plant("Sunflower", 80, 45),
        plant("Cactus", 15, 120),
    ]
    for p in plants:
        p.show()
