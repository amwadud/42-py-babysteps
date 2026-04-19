from collections.abc import Callable


def spell_combiner(
    spell1: Callable[[str, int], str], spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combined


def power_amplifier(
    base_spell: Callable[[str, int], str], multiplier: int
) -> Callable[[str, int], str]:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(
    condition: Callable[[str, int], bool], spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional


def spell_sequence(
    spells: list[Callable[[str, int], str]],
) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence


def main():
    # Sample spells to test with
    def fireball(target: str, _power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, _power: int) -> str:
        return f"Heals {target}"

    print(" Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f" Combined spell result: {result[0]}, {result[1]}")

    print("\n Testing power amplifier...")
    original_power = 10
    amplified_power = original_power * 3
    print(f" Original: {original_power}, Amplified: {amplified_power}")

    print("\n Testing conditional caster...")

    def always_true(_target: str, power: int) -> bool:
        return power > 5

    conditional_fire = conditional_caster(always_true, fireball)
    print(f" Condition met: {conditional_fire('Dragon', 10)}")
    print(f" Condition failed: {conditional_fire('Dragon', 2)}")

    print("\n Testing spell sequence...")
    seq = spell_sequence([fireball, heal])
    print(f" Sequence: {seq('Dragon', 10)}")


if __name__ == "__main__":
    main()
