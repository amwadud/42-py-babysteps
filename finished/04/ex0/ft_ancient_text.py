#!/usr/bin/env python3


from sys import stderr


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===", end="\n\n")
    filepath = "ancient_fragment.txt"
    try:
        f = open(filepath)
        print("Connection established...", end="\n\n")
        print("RECOVERED DATA:")
        print(f.read(), end="\n\n")
        print("Data recovery complete. Storage unit disconnected.")
        f.close()
    except (FileNotFoundError, PermissionError, IsADirectoryError):
        print("ERROR: Storage vault not found.", file=stderr)


if __name__ == "__main__":
    main()
