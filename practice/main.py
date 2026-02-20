#!/usr/bin/env python3

# Write for me a module as exmaple, to practice modules in python.


class TestModule:
    def __init__(self, name: str) -> None:
        self.name = name

    def greet() -> str:
        return "Hello world!"

    great = staticmethod(greet)


if __name__ == "__main__":
    TestModule.greet()
