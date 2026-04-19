from collections.abc import Callable
from functools import reduce, lru_cache, singledispatch, partial
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    if operation in ("max", "min"):
        return operations[operation](spells)

    op = operations[operation]
    return reduce(lambda x, y: op(x, y), spells)


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str],
) -> dict[str, Callable[[str], str]]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@singledispatch
def spell_dispatcher(spell_data: object) -> str:
    return "Unknown spell type"


@spell_dispatcher.register(int)
def _(spell_data: int) -> str:
    return f"{spell_data} damage"


@spell_dispatcher.register(str)
def _(spell_data: str) -> str:
    return spell_data


@spell_dispatcher.register(list)
def _(spell_data: list[object]) -> str:
    return f"{len(spell_data)} spells"


def main():
    spells = [10, 20, 30, 40]

    print(" Testing spell reducer...")
    print(f" Sum: {spell_reducer(spells, 'add')}")
    print(f" Product: {spell_reducer(spells, 'multiply')}")
    print(f" Max: {spell_reducer(spells, 'max')}")

    print("\n Testing memoized fibonacci...")
    print(f" Fib(0): {memoized_fibonacci(0)}")
    print(f" Fib(1): {memoized_fibonacci(1)}")
    print(f" Fib(10): {memoized_fibonacci(10)}")
    print(f" Fib(15): {memoized_fibonacci(15)}")
    print(f" Cache info: {memoized_fibonacci.cache_info()}")

    print("\n Testing spell dispatcher...")
    print(f" Damage spell: {spell_dispatcher(42)}")
    print(f" Enchantment: {spell_dispatcher('fireball')}")
    print(f" Multi-cast: {spell_dispatcher(['a', 'b', 'c'])}")
    print(f" Unknown: {spell_dispatcher(3.14)}")


if __name__ == "__main__":
    main()
