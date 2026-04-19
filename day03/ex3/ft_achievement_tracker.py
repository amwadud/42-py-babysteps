#!/usr/bin/env python3


def display_achievement(name: str, ach: set[str]) -> None:
    """Print players achievements."""
    print(f"Player {name} achievements: {ach}")


def achievement_tracker() -> None:
    """Track and analyze player achievements using Set operations."""
    players: dict[str, set[str]] = {
        "alice": {
            "first_kill",
            "level_10",
            "treasure_hunter",
            "speed_demon",
        },
        "bob": {"first_kill", "level_10", "boss_slayer", "collector"},
        "charlie": {
            "level_10",
            "treasure_hunter",
            "boss_slayer",
            "speed_demon",
            "perfectionist",
        },
    }
    alice: set[str] = players["alice"]
    bob: set[str] = players["bob"]
    charlie: set[str] = players["charlie"]

    print("=== Achievement Tracker System ===")
    for name, ach in players.items():
        display_achievement(name, ach)

    print("\n=== Achievement Analytics ===")

    # Analytics: All unique achievements (Union)
    all_unique = alice.union(bob, charlie)
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}")

    # Analytics: Shared achievements (Intersection)
    common_all = alice.intersection(bob, charlie)
    print(f"Common to all players: {common_all}")

    # Analytics: Rare achievements (Unique to exactly 1 player)
    only_alice = alice.difference(bob.union(charlie))
    only_bob = bob.difference(alice.union(charlie))
    only_charlie = charlie.difference(alice.union(bob))

    # union() can take multiple arguments at once
    rare = only_alice.union(only_bob, only_charlie)
    print(f"Rare achievements (1 player): {rare}")
    print()

    # Comparisons
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


def main() -> None:
    achievement_tracker()


if __name__ == "__main__":
    main()
