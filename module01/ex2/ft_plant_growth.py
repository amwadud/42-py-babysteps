#!/usr/bin/env python3


class plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int = 1):
        self.height += cm

    def grow_older(self, days: int = 1):
        self.age += days

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    p1 = plant("Rose", 30, 15)
    prev_height = p1.height
    print("== Day 1 ==")
    p1.show()
    p1.grow(5)
    p1.grow_older(5)
    print("== Day 7 ==")
    p1.show()
    print(f"Growth this week: +{p1.height - prev_height}")
