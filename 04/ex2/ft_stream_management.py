#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    try:
        id = input("Input Stream active. Enter archivist ID: ")
        status_report = input("Input Stream active. Enter status report: ")
        print()
        print(
            f"[STANDARD] Archive status from {id}: {status_report}",
            file=sys.stdout,
        )
        print(
            "[ALERT] System diagnostic: Communication channels verified",
            file=sys.stderr,
        )
        print("[STANDARD] Data transmission complete", file=sys.stdout)
    except EOFError:
        print(
            "\n[ALERT] Input stream interrupted. Connection lost.",
            file=sys.stderr,
        )
    except KeyboardInterrupt:
        print("\n[ALERT] Archivist cancelled the operation.", file=sys.stderr)
    except Exception as e:
        print(f"\n[ALERT] Unexpected system failure: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
