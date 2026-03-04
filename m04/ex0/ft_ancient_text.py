#!/usr/bin/env python3


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===", end="\n\n")
    filepath = input("Accessing Storage Vault: ")
    try:
        with open(filepath) as f:
            print("Connection established...", end="\n\n")
            print("RECOVERED DATA:")
            print(f.read())
            print("Data recovery complete. Storage unit disconnected.")
    except (FileNotFoundError, PermissionError, IsA


if __name__ == "__main__":
    main()
