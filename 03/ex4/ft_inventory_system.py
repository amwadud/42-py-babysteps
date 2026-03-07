#!/usr/bin/env python3

import sys


def ft_inventory_system() -> None:
    """Master game inventory management using dictionaries."""
    inventory: dict[str, int] = {}

    # 1. Parsing Input
    if len(sys.argv) == 1:
        print("=== Inventory System Analysis ===")
        print(
            "No scores provided. Usage: python3 ft_inventory_system.py "
            + "<item1:count1> <item2:count2> ..."
        )
        return

    for arg in sys.argv[1:]:
        inventory[arg.split(":")[0]] = int(arg.split(":")[1])

    if not inventory:
        return

    # 2. System Analysis
    # Calculate total once (efficient Data Engineering)
    total_items: int = sum(inventory.values())
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    # 3. Current Inventory
    print("\n=== Current Inventory ===")
    for key, val in inventory.items():
        percentage: float = (val / total_items) * 100
        print(f"{key}: {val} units ({percentage:.1f}%)")

    # 4. Inventory Statistics
    print("\n=== Inventory Statistics ===")
    # Passing the .get method directly to find the key with the max/min value
    most: str = max(inventory, key=inventory.get)
    least: str = min(inventory, key=inventory.get)
    print(f"Most abundant: {most} ({inventory[most]} units)")
    print(f"Least abundant: {least} ({inventory[least]} unit)")

    # 5. Item Categories (Nested Dictionaries)
    print("\n=== Item Categories ===")
    # Note capitalization to match PDF
    categories: dict[str, dict[str, int]] = {"Moderate": {}, "Scarce": {}}

    for item, count in inventory.items():
        if count >= 5:
            categories["Moderate"][item] = count
        else:
            categories["Scarce"][item] = count

    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")

    # 6. Management Suggestions
    print("\n=== Management Suggestions ===")
    # Join keys with a comma to match "Restock needed: sword, helmet"
    restock_list = ", ".join(categories["Scarce"].keys())
    print(f"Restock needed: {restock_list}")

    # 7. Dictionary Properties Demo
    print("\n=== Dictionary Properties Demo ===")
    # Using unpacking (*) to print clean lists without trailing commas
    print("Dictionary keys: ", end="")
    print(*inventory.keys(), sep=", ")

    print("Dictionary values: ", end="")
    print(*inventory.values(), sep=", ")

    # Safe lookup using "in"
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


def main() -> None:
    ft_inventory_system()


if __name__ == "__main__":
    main()
