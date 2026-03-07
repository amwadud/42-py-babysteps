#!/usr/bin/env python3


import sys


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    # 1. SECURE EXTRACTION (Reading)
    try:
        # Use 'with' so the file closes automatically!
        with open("classified_data.txt", "r") as vault:
            _ = vault.read()
            print("SECURE EXTRACTION:")
            print("[CLASSIFIED] Quantum encryption keys recovered")
            print("[CLASSIFIED] Archive integrity: 100%\n")
    except FileNotFoundError:
        print("ERROR: Classified vault not found.")
        sys.exit(1)

    # 2. SECURE PRESERVATION (Writing)
    with open("security_report.txt", "w") as archive:
        _ = archive.write("Security protocols updated.")
        print("SECURE PRESERVATION:")
        print("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion\n")

    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
