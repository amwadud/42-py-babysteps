#!/usr/bin/env python3


def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===", end="\n\n")
    filepath = "new_discovery.txt"
    try:
        print(f"Initializing new storage unit: {filepath}", end="\n\n")
        f = open(filepath, "w")
        print("Storage unit created successfully...", end="\n\n")
        print("Inscribing preservation data...")
        print(
            "{[}ENTRY 001{]} New quantum algorithm discovered\n"
            + "{[}ENTRY 002{]} Efficiency increased by 347%\n"
            + "{[}ENTRY 003{]} Archived by Data Archivist trainee",
            end="\n\n",
        )
        _ = f.write(
            "{[}ENTRY 001{]} New quantum algorithm discovered\n"
            + "{[}ENTRY 002{]} Efficiency increased by 347%\n"
            + "{[}ENTRY 003{]} Archived by Data Archivist trainee"
        )
        print(
            "Data inscription complete. Storage unit sealed.\n"
            + f"Archive '{filepath}' ready for long-term"
            + " preservation."
        )
        f.close()
    except Exception:
        print("ERROR: Something went wrong.")


if __name__ == "__main__":
    main()
