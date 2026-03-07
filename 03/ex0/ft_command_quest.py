#!/usr/bin/env python3
"""
Command Quest - A simple command-line argument interpreter.
Displays program name, arguments received, and total argument count.
"""

import sys


def main() -> None:
    """Parse and display command-line arguments in a formatted way."""
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len(sys.argv) - 1}")
        i = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
