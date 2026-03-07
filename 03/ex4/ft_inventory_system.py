#!/usr/bin/env python3

import sys


def ft_inventory_system() -> None:
    inventory: dict[str, int] = {}
    # Init data dict
    for arg in sys.argv[1:]:
        inventory[arg.split(":")[0]] = int(arg.split(":")[1])
    print("\n=== Inventory System Analysis ===")
    print("Total items in inventory: ", sum(inventory.values()))
    print("Unique item types: ", len(inventory))

    print("\n=== Current Inventory ===")
    for key, val in inventory.items():
        percentage = (val / sum(inventory.values())) * 100
        print(f"{key}: {val} units ({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")
    most = inventory[max(inventory, key=inventory.get)]
    least = inventory[min(inventory, key=inventory.get)]
    print(f"Most abundant: {max(inventory, key=inventory.get)} ({most} units)")
    print(
        f"Least abundant: {min(inventory, key=inventory.get)} ({least} unit)"
    )

    print("\n=== Item Categories ===")
    print("\n=== Management Suggestions ===")
    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary keys: ", end="")
    print(*inventory.keys(), sep=", ")
    print("Dictionary values: ", end="")
    print(*inventory.values(), sep=", ")
    print(
        "Sample lookup - 'sword' in inventory: ", "sword" in inventory.keys()
    )


def main() -> None:
    ft_inventory_system()


if __name__ == "__main__":
    main()
