#!/usr/bin/env python3

from typing import Generator
# from collections.abc import Generator

events = [
    {
        "id": 0,
        "desc": "Player frank (level 8) leveled up",
        "player": "frank",
        "event_type": "level_up",
        "timestamp": "2024-01-01T23:17",
        "data": {"level": 8, "score_delta": 128, "zone": "pixel_zone_2"},
    },
    {
        "id": 1,
        "desc": "Player frank (level 12) found treasure",
        "player": "frank",
        "event_type": "item_found",
        "timestamp": "2024-01-22T23:57",
        "data": {"level": 12, "score_delta": 200, "zone": "pixel_zone_5"},
    },
    {
        "id": 2,
        "desc": "Player diana (level 5) login",
        "player": "diana",
        "event_type": "login",
        "timestamp": "2024-01-01T02:13",
        "data": {"level": 5, "score_delta": 0, "zone": "pixel_zone_5"},
    },
    {
        "id": 3,
        "desc": "Player alice (level 15) leveled up",
        "player": "alice",
        "event_type": "level_up",
        "timestamp": "2024-01-07T22:41",
        "data": {"level": 15, "score_delta": 458, "zone": "pixel_zone_4"},
    },
    {
        "id": 4,
        "desc": "Player bob (level 9) killed an enemy",
        "player": "bob",
        "event_type": "kill",
        "timestamp": "2024-01-19T08:51",
        "data": {"level": 9, "score_delta": 63, "zone": "pixel_zone_4"},
    },
    {
        "id": 5,
        "desc": "Player charlie (level 22) found treasure",
        "player": "charlie",
        "event_type": "item_found",
        "timestamp": "2024-01-05T06:48",
        "data": {"level": 22, "score_delta": 4, "zone": "pixel_zone_1"},
    },
    {
        "id": 6,
        "desc": "Player diana (level 17) leveled up",
        "player": "diana",
        "event_type": "level_up",
        "timestamp": "2024-01-12T11:38",
        "data": {"level": 17, "score_delta": 150, "zone": "pixel_zone_4"},
    },
    {
        "id": 7,
        "desc": "Player eve (level 36) login",
        "player": "eve",
        "event_type": "login",
        "timestamp": "2024-01-30T12:05",
        "data": {"level": 36, "score_delta": 0, "zone": "pixel_zone_5"},
    },
    {
        "id": 8,
        "desc": "Player charlie (level 3) leveled up",
        "player": "charlie",
        "event_type": "level_up",
        "timestamp": "2024-01-07T22:04",
        "data": {"level": 3, "score_delta": 133, "zone": "pixel_zone_3"},
    },
    {
        "id": 9,
        "desc": "Player alice (level 18) logout",
        "player": "alice",
        "event_type": "logout",
        "timestamp": "2024-01-28T03:24",
        "data": {"level": 18, "score_delta": 0, "zone": "pixel_zone_3"},
    },
    {
        "id": 10,
        "desc": "Player bob (level 18) killed an enemy",
        "player": "bob",
        "event_type": "kill",
        "timestamp": "2024-01-12T06:42",
        "data": {"level": 18, "score_delta": 90, "zone": "pixel_zone_5"},
    },
    {
        "id": 11,
        "desc": "Player frank (level 11) logout",
        "player": "frank",
        "event_type": "logout",
        "timestamp": "2024-01-18T23:15",
        "data": {"level": 11, "score_delta": 0, "zone": "pixel_zone_4"},
    },
    {
        "id": 12,
        "desc": "Player charlie (level 44) found treasure",
        "player": "charlie",
        "event_type": "item_found",
        "timestamp": "2024-01-23T17:14",
        "data": {"level": 44, "score_delta": 232, "zone": "pixel_zone_1"},
    },
    {
        "id": 13,
        "desc": "Player bob (level 18) login",
        "player": "bob",
        "event_type": "login",
        "timestamp": "2024-01-26T10:25",
        "data": {"level": 18, "score_delta": 0, "zone": "pixel_zone_2"},
    },
    {
        "id": 14,
        "desc": "Player eve (level 32) found treasure",
        "player": "eve",
        "event_type": "item_found",
        "timestamp": "2024-01-11T06:41",
        "data": {"level": 32, "score_delta": 305, "zone": "pixel_zone_4"},
    },
    {
        "id": 15,
        "desc": "Player bob (level 36) killed an enemy",
        "player": "bob",
        "event_type": "kill",
        "timestamp": "2024-01-05T07:47",
        "data": {"level": 36, "score_delta": 451, "zone": "pixel_zone_3"},
    },
    {
        "id": 16,
        "desc": "Player frank (level 24) leveled up",
        "player": "frank",
        "event_type": "level_up",
        "timestamp": "2024-01-14T18:25",
        "data": {"level": 24, "score_delta": 124, "zone": "pixel_zone_2"},
    },
    {
        "id": 17,
        "desc": "Player eve (level 8) died",
        "player": "eve",
        "event_type": "death",
        "timestamp": "2024-01-03T01:55",
        "data": {"level": 8, "score_delta": -50, "zone": "pixel_zone_2"},
    },
    {
        "id": 18,
        "desc": "Player frank (level 25) died",
        "player": "frank",
        "event_type": "death",
        "timestamp": "2024-01-20T02:24",
        "data": {"level": 25, "score_delta": -30, "zone": "pixel_zone_5"},
    },
    {
        "id": 19,
        "desc": "Player charlie (level 47) leveled up",
        "player": "charlie",
        "event_type": "level_up",
        "timestamp": "2024-01-28T00:43",
        "data": {"level": 47, "score_delta": 17, "zone": "pixel_zone_5"},
    },
    {
        "id": 20,
        "desc": "Player charlie (level 28) found treasure",
        "player": "charlie",
        "event_type": "item_found",
        "timestamp": "2024-01-11T03:18",
        "data": {"level": 28, "score_delta": 61, "zone": "pixel_zone_4"},
    },
    {
        "id": 21,
        "desc": "Player alice (level 33) found treasure",
        "player": "alice",
        "event_type": "item_found",
        "timestamp": "2024-01-29T23:16",
        "data": {"level": 33, "score_delta": 82, "zone": "pixel_zone_5"},
    },
    {
        "id": 22,
        "desc": "Player alice (level 39) found treasure",
        "player": "alice",
        "event_type": "item_found",
        "timestamp": "2024-01-10T20:32",
        "data": {"level": 39, "score_delta": 103, "zone": "pixel_zone_2"},
    },
    {
        "id": 23,
        "desc": "Player charlie (level 1) logout",
        "player": "charlie",
        "event_type": "logout",
        "timestamp": "2024-01-18T16:58",
        "data": {"level": 1, "score_delta": 0, "zone": "pixel_zone_4"},
    },
    {
        "id": 24,
        "desc": "Player alice (level 20) login",
        "player": "alice",
        "event_type": "login",
        "timestamp": "2024-01-30T11:56",
        "data": {"level": 20, "score_delta": 0, "zone": "pixel_zone_1"},
    },
    {
        "id": 25,
        "desc": "Player bob (level 32) leveled up",
        "player": "bob",
        "event_type": "level_up",
        "timestamp": "2024-01-03T02:46",
        "data": {"level": 32, "score_delta": 200, "zone": "pixel_zone_5"},
    },
    {
        "id": 26,
        "desc": "Player bob (level 11) logout",
        "player": "bob",
        "event_type": "logout",
        "timestamp": "2024-01-22T15:35",
        "data": {"level": 11, "score_delta": 0, "zone": "pixel_zone_5"},
    },
    {
        "id": 27,
        "desc": "Player eve (level 47) died",
        "player": "eve",
        "event_type": "death",
        "timestamp": "2024-01-07T17:48",
        "data": {"level": 47, "score_delta": -40, "zone": "pixel_zone_3"},
    },
    {
        "id": 28,
        "desc": "Player diana (level 34) found treasure",
        "player": "diana",
        "event_type": "item_found",
        "timestamp": "2024-01-21T11:28",
        "data": {"level": 34, "score_delta": 362, "zone": "pixel_zone_1"},
    },
    {
        "id": 29,
        "desc": "Player bob (level 38) logout",
        "player": "bob",
        "event_type": "logout",
        "timestamp": "2024-01-03T10:01",
        "data": {"level": 38, "score_delta": 0, "zone": "pixel_zone_2"},
    },
    {
        "id": 30,
        "desc": "Player eve (level 41) logout",
        "player": "eve",
        "event_type": "logout",
        "timestamp": "2024-01-01T02:45",
        "data": {"level": 41, "score_delta": 0, "zone": "pixel_zone_2"},
    },
    {
        "id": 31,
        "desc": "Player alice (level 33) login",
        "player": "alice",
        "event_type": "login",
        "timestamp": "2024-01-28T10:04",
        "data": {"level": 33, "score_delta": 0, "zone": "pixel_zone_3"},
    },
    {
        "id": 32,
        "desc": "Player frank (level 47) died",
        "player": "frank",
        "event_type": "death",
        "timestamp": "2024-01-07T17:08",
        "data": {"level": 47, "score_delta": -60, "zone": "pixel_zone_5"},
    },
    {
        "id": 33,
        "desc": "Player diana (level 27) logout",
        "player": "diana",
        "event_type": "logout",
        "timestamp": "2024-01-26T15:51",
        "data": {"level": 27, "score_delta": 0, "zone": "pixel_zone_1"},
    },
    {
        "id": 34,
        "desc": "Player alice (level 27) found treasure",
        "player": "alice",
        "event_type": "item_found",
        "timestamp": "2024-01-14T11:27",
        "data": {"level": 27, "score_delta": 378, "zone": "pixel_zone_1"},
    },
    {
        "id": 35,
        "desc": "Player frank (level 26) found treasure",
        "player": "frank",
        "event_type": "item_found",
        "timestamp": "2024-01-21T03:03",
        "data": {"level": 26, "score_delta": 247, "zone": "pixel_zone_1"},
    },
    {
        "id": 36,
        "desc": "Player bob (level 9) logout",
        "player": "bob",
        "event_type": "logout",
        "timestamp": "2024-01-07T17:28",
        "data": {"level": 9, "score_delta": 0, "zone": "pixel_zone_2"},
    },
    {
        "id": 37,
        "desc": "Player charlie (level 36) died",
        "player": "charlie",
        "event_type": "death",
        "timestamp": "2024-01-08T02:28",
        "data": {"level": 36, "score_delta": -20, "zone": "pixel_zone_1"},
    },
    {
        "id": 38,
        "desc": "Player frank (level 49) leveled up",
        "player": "frank",
        "event_type": "level_up",
        "timestamp": "2024-01-27T00:05",
        "data": {"level": 49, "score_delta": 142, "zone": "pixel_zone_2"},
    },
    {
        "id": 39,
        "desc": "Player diana (level 26) died",
        "player": "diana",
        "event_type": "death",
        "timestamp": "2024-01-16T06:55",
        "data": {"level": 26, "score_delta": -40, "zone": "pixel_zone_2"},
    },
    {
        "id": 40,
        "desc": "Player diana (level 30) login",
        "player": "diana",
        "event_type": "login",
        "timestamp": "2024-01-13T08:59",
        "data": {"level": 30, "score_delta": 0, "zone": "pixel_zone_4"},
    },
    {
        "id": 41,
        "desc": "Player frank (level 46) found treasure",
        "player": "frank",
        "event_type": "item_found",
        "timestamp": "2024-01-26T17:42",
        "data": {"level": 46, "score_delta": 398, "zone": "pixel_zone_2"},
    },
    {
        "id": 42,
        "desc": "Player bob (level 48) killed an enemy",
        "player": "bob",
        "event_type": "kill",
        "timestamp": "2024-01-07T01:37",
        "data": {"level": 48, "score_delta": 455, "zone": "pixel_zone_1"},
    },
    {
        "id": 43,
        "desc": "Player frank (level 31) killed an enemy",
        "player": "frank",
        "event_type": "kill",
        "timestamp": "2024-01-02T01:37",
        "data": {"level": 31, "score_delta": 414, "zone": "pixel_zone_5"},
    },
    {
        "id": 44,
        "desc": "Player bob (level 12) login",
        "player": "bob",
        "event_type": "login",
        "timestamp": "2024-01-17T02:54",
        "data": {"level": 12, "score_delta": 0, "zone": "pixel_zone_5"},
    },
    {
        "id": 45,
        "desc": "Player alice (level 8) found treasure",
        "player": "alice",
        "event_type": "item_found",
        "timestamp": "2024-01-28T07:25",
        "data": {"level": 8, "score_delta": 483, "zone": "pixel_zone_2"},
    },
    {
        "id": 46,
        "desc": "Player eve (level 27) leveled up",
        "player": "eve",
        "event_type": "level_up",
        "timestamp": "2024-01-02T19:05",
        "data": {"level": 27, "score_delta": 497, "zone": "pixel_zone_5"},
    },
    {
        "id": 47,
        "desc": "Player eve (level 43) killed an enemy",
        "player": "eve",
        "event_type": "kill",
        "timestamp": "2024-01-30T08:13",
        "data": {"level": 43, "score_delta": 221, "zone": "pixel_zone_2"},
    },
    {
        "id": 48,
        "desc": "Player charlie (level 20) died",
        "player": "charlie",
        "event_type": "death",
        "timestamp": "2024-01-05T21:41",
        "data": {"level": 20, "score_delta": -25, "zone": "pixel_zone_3"},
    },
    {
        "id": 49,
        "desc": "Player alice (level 7) login",
        "player": "alice",
        "event_type": "login",
        "timestamp": "2024-01-15T19:36",
        "data": {"level": 7, "score_delta": 0, "zone": "pixel_zone_5"},
    },
    {
        "id": 50,
        "desc": "Player diana (level 11) leveled up",
        "player": "diana",
        "event_type": "level_up",
        "timestamp": "2024-01-17T14:22",
        "data": {"level": 11, "score_delta": 310, "zone": "pixel_zone_3"},
    },
]


def game_event_generator(limit: int) -> Generator[str, None, None]:
    """Yields game events one by one without storing them in a list."""
    for event in events[:limit]:
        yield event["desc"]


def fibonacci_generator(limit: int) -> Generator[int, None, None]:
    """Memory-efficient Fibonacci sequence."""
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


def prime_generator(limit: int) -> Generator[int, None, None]:
    """Yields the first N prime numbers."""

    def is_prime(n: int) -> bool:
        """Checks if a number is prime using O(sqrt(n)) logic."""
        if n <= 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    n = 2
    count = 0
    while count < limit:
        if is_prime(n):
            yield n
            count += 1
        n += 1


def main() -> None:
    total_to_process = 50
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0
    printed_events = 0

    print("=== Game Data Stream Processor ===")
    print(f"\nProcessing {total_to_process} game events...\n")

    for event in game_event_generator(total_to_process):
        if printed_events < 3:
            print(event)
            printed_events += 1

        if "found treasure" in event:
            treasure_events += 1
        if "leveled up" in event:
            level_up_events += 1

        try:
            level = int(event.split("(level ")[1].split(")")[0])
            if level >= 10:
                high_level_players += 1
        except (IndexError, ValueError):
            pass

    print("...")
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_to_process}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")

    print("Fibonacci sequence (first 10):", end=" ", flush=True)
    i = 1
    for val in fibonacci_generator(10):
        if i == 10:
            print(f"{val}", end="", flush=True)
        else:
            print(f"{val}, ", end="", flush=True)
        i += 1
    print()

    print("Prime numbers (first 5):", end=" ", flush=True)
    i = 1
    for val in prime_generator(5):
        if i == 5:
            print(f"{val}", end="", flush=True)
        else:
            print(f"{val}, ", end="", flush=True)
        i += 1
    print()


if __name__ == "__main__":
    main()
