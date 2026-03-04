#!/usr/bin/env python3

import sys


def usage() -> None:
    print(
        "No scores provided. "
        + " Usage: python3 ft_score_analytics.py <score1> <score2> ..."
    )


def display_player_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    scores: list[int] = []
    try:
        scores = [int(x) for x in sys.argv[1:]]
    except ValueError:
        raise ValueError("Scores should be integers only.")
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Average score: {float(sum(scores)) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


def main() -> None:
    if len(sys.argv) == 1:
        usage()
        return
    try:
        display_player_score_analytics()
    except ValueError as error:
        print(f"[ERROR]: {error}")


if __name__ == "__main__":
    main()
