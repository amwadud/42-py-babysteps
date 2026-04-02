#!/usr/bin/env python3
"""
Exercise 6: Data Alchemist
Mastering list, dict, and set comprehensions for data engineering.
"""

data = {
    "players": {
        "alice": {
            "level": 41,
            "total_score": 2824,
            "sessions_played": 13,
            "favorite_mode": "ranked",
            "achievements_count": 5,
        },
        "bob": {
            "level": 16,
            "total_score": 4657,
            "sessions_played": 27,
            "favorite_mode": "ranked",
            "achievements_count": 2,
        },
        "charlie": {
            "level": 44,
            "total_score": 9935,
            "sessions_played": 21,
            "favorite_mode": "ranked",
            "achievements_count": 7,
        },
        "diana": {
            "level": 3,
            "total_score": 1488,
            "sessions_played": 21,
            "favorite_mode": "casual",
            "achievements_count": 4,
        },
        "eve": {
            "level": 33,
            "total_score": 1434,
            "sessions_played": 81,
            "favorite_mode": "casual",
            "achievements_count": 7,
        },
        "frank": {
            "level": 15,
            "total_score": 8359,
            "sessions_played": 85,
            "favorite_mode": "competitive",
            "achievements_count": 1,
        },
    },
    "sessions": [
        {
            "player": "bob",
            "duration_minutes": 94,
            "score": 1831,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "bob",
            "duration_minutes": 32,
            "score": 1478,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 17,
            "score": 1570,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 98,
            "score": 1981,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 15,
            "score": 2361,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "eve",
            "duration_minutes": 29,
            "score": 2985,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 34,
            "score": 1285,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "alice",
            "duration_minutes": 53,
            "score": 1238,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 1555,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "frank",
            "duration_minutes": 92,
            "score": 2754,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 98,
            "score": 1102,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "diana",
            "duration_minutes": 39,
            "score": 2721,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 46,
            "score": 329,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 56,
            "score": 1196,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 117,
            "score": 1388,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "diana",
            "duration_minutes": 118,
            "score": 2733,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 22,
            "score": 1110,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "frank",
            "duration_minutes": 79,
            "score": 1854,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "charlie",
            "duration_minutes": 33,
            "score": 666,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 101,
            "score": 292,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 25,
            "score": 2887,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 53,
            "score": 2540,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "eve",
            "duration_minutes": 115,
            "score": 147,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 118,
            "score": 2299,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 42,
            "score": 1880,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 97,
            "score": 1178,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 18,
            "score": 2661,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 761,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 46,
            "score": 2101,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 117,
            "score": 1359,
            "mode": "casual",
            "completed": True,
        },
    ],
    "active_regions": {"north", "east", "central"},
    "game_modes": ["casual", "competitive", "ranked"],
    "achievements": [
        "first_blood",
        "level_master",
        "speed_runner",
        "treasure_seeker",
        "boss_hunter",
        "pixel_perfect",
        "combo_king",
        "explorer",
    ],
}

# === Lists


def high_scorers() -> list[str]:
    """Returns names of players with total score above 2000."""
    return [
        name
        for name, stat in data["players"].items()
        if stat["total_score"] > 2000
    ]


def scores_doubled() -> list[int]:
    """Returns every player's total score multiplied by 2."""
    return [stat["total_score"] * 2 for stat in data["players"].values()]


def active_players() -> list[str]:
    """Returns names of players with at least one incomplete session."""
    return [
        session["player"]
        for session in data["sessions"]
        if not session["completed"]
    ]


# === Dict


def player_scores() -> dict[str, int]:
    """Returns a mapping of player name to their total score."""
    return {
        name: stat["total_score"] for name, stat in data["players"].items()
    }


def score_categories() -> dict[str, int]:
    """Returns count of players in high (>=5000), medium (2000-4999), and low (<2000) score ranges."""
    return {
        "high": len(
            [
                stat["total_score"]
                for name, stat in data["players"].items()
                if stat["total_score"] >= 5000
            ]
        ),
        "medium": len(
            [
                stat["total_score"]
                for name, stat in data["players"].items()
                if 2000 <= stat["total_score"] < 5000
            ]
        ),
        "low": len(
            [
                stat["total_score"]
                for name, stat in data["players"].items()
                if stat["total_score"] < 2000
            ]
        ),
    }


def ach_count() -> dict[str, int]:
    """Returns a mapping of player name to their achievements count."""
    return {
        name: stat["achievements_count"]
        for name, stat in data["players"].items()
    }


# === Sets


def unique_players() -> set[str]:
    """Returns the set of players who have at least one session."""
    return {player["player"] for player in data["sessions"]}


def unique_achievements() -> set[str]:
    """Returns the set of all available achievements."""
    return {ach for ach in data["achievements"]}


def active_regions() -> set[str]:
    """Returns the set of currently active regions."""
    return {region for region in data["active_regions"]}


# === Mics


def total_players() -> int:
    """Returns the total number of unique players."""
    return len({name for name, stat in data["players"].items()})


def total_unique_achievements() -> int:
    """Returns the total number of unique achievements."""
    return len(data["achievements"])


def average_score() -> int:
    """Returns the average total score across all players."""
    return (
        sum([stat["total_score"] for name, stat in data["players"].items()])
        / total_players()
    )


def top_performer() -> str:
    """Returns the name of the player with the highest total score."""
    scores = player_scores()
    return max(scores, key=scores.get)


def main() -> None:
    """
    Processes gaming data using comprehensions to generate a dashboard.
    """
    players = data["players"]
    sessions = data["sessions"]

    print("=== Game Analytics Dashboard ===")
    print()
    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {high_scorers()}")
    print(f"Scores doubled: {scores_doubled()}")
    print(f"Active players: {active_players()}")
    print()
    print("=== Dict Comprehension Examples ===")
    print(f"Player scores: {player_scores()}")
    print(f"Score categories: {score_categories()}")
    print(f"Achievement counts: {ach_count()}")
    print()
    print("=== Set Comprehension Examples ===")
    print(f"Unique players: {unique_players()}")
    print(f"Unique achievements: {unique_achievements()}")
    print(f"Active regions: {active_regions()}")
    print()
    print("=== Combined Analysis ===")
    print(f"Total players: {total_players()}")
    print(f"Total unique achievements: {total_unique_achievements()}")
    print(f"Average score: {average_score():.2f}")
    print(f"Top performer: {top_performer()}")


if __name__ == "__main__":
    main()
