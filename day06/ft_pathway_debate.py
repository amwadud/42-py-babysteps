import alchemy.transmutation

print("=== Pathway Debate Mastery ===")

print("\nTesting Absolute Imports (from basic.py):")
print("lead_to_gold():", alchemy.transmutation.lead_to_gold())
print("stone_to_gem():", alchemy.transmutation.stone_to_gem())

print("\nTesting Relative Imports (from advanced.py):")
print("philosophers_stone():", alchemy.transmutation.philosophers_stone())
print("elixir_of_life():", alchemy.transmutation.elixir_of_life())

print("\nTesting Package Access:")
print(
    "alchemy.transmutation.lead_to_gold():",
    alchemy.transmutation.lead_to_gold(),
)
print(
    "alchemy.transmutation.philosophers_stone():",
    alchemy.transmutation.philosophers_stone(),
)

print("\nBoth pathways work! Absolute: clear, Relative: concise")
