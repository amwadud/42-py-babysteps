#!/usr/bin/env python3
import sys


def display_stats(scores: list[int]) -> None:
    """Calculate and display statistics from a list of scores."""
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


def usage() -> None:
    print(
        "No scores provided. Usage: python3 ft_score_analytics.py "
        + "<score1> <score2> ..."
    )


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        usage()
        return

    try:
        scores = [int(arg) for arg in sys.argv[1:]]
        display_stats(scores)
    except ValueError:
        print("[ERROR]: Scores should be integers only.")


if __name__ == "__main__":
    main()
