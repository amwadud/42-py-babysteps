#!/usr/bin/env python3


def check_temperature(temp_str: str) -> None:
    try:
        val = int(temp_str)
        if val > 40:
            print("Error: ", val, "°C is too hot for plants (max 40°C)")
        elif val < 0:
            print("Error: ", val, "°C is too cold for plants (min 0°C)")
        else:
            print("Temperature ", val, "°C is perfect for plants!")

    except ValueError:
        print("That's not a valid number!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    vals = ["25", "abc", "100", "-50"]

    for val in vals:
        print("Testing temperature: ", val)
        check_temperature(val)
        print()

    print("All tests completed - program didn't crash!")
