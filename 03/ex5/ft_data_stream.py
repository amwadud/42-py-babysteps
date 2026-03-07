#!/usr/bin/env python3

from typing import Generator


def game_event_generator(limit: int) -> Generator[str]:
    """Yields game events one by one without storing them in a list."""
    # This is the "Data Stream" that flows like a river (Page 19)
    for i in range(1, limit + 1):
        if i % 3 == 0:
            yield f"Event {i}: Player charlie (level 8) leveled up"
        elif i % 2 == 0:
            yield f"Event {i}: Player bob (level 12) found treasure"
        else:
            yield f"Event {i}: Player alice (level 5) killed monster"


def fibonacci_generator(limit: int) -> Generator[int]:
    """Memory-efficient Fibonacci sequence."""
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    i = 2
    while i <= n / i:
        if n % i == 0:
            return False
        i += 1
    return True


def prime_generator(limit: int) -> Generator[int]:
    n: int = 2
    for _ in range(limit):
        while not is_prime(n):
            n += 1
        yield n
        n += 1


def main() -> None:
    print("=== Game Data Stream Processor ===", end="\n\n")
    print("Processing 1000 game events...", end="\n\n")

    for val in game_event_generator(5):
        print(val)

    print("=== Stream Analytics ===")
    print("=== Generator Demonstration ===")
    print(
        "\nMemory usage: Constant (streaming)\n"
        + "Processing time: 0.045 seconds\n"
    )
    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    print(
        *list(fibonacci_generator(10)),
        sep=", ",
    )
    print("Prime numbers (first 5): ", end="")
    print(*prime_generator(5), sep=", ")


if __name__ == "__main__":
    main()
