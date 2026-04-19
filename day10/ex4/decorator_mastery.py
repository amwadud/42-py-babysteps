import time
from collections.abc import Callable
from functools import wraps
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return wrapper  # type: ignore[return-value]


def power_validator(
    min_power: int,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power: int = 0
            if args:
                first_arg = args[0]
                if isinstance(first_arg, int):
                    power = first_arg
                elif len(args) > 2 and isinstance(args[2], int):
                    power = args[2]
                else:
                    power = kwargs.get("power", 0)
            else:
                power = kwargs.get("power", 0)

            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)

        return wrapper  # type: ignore[return-value]

    return decorator


def retry_spell(
    max_attempts: int,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        msg = (
                            "Spell failed, retrying... "
                            + f"(attempt {attempt}/{max_attempts})"
                        )
                        print(msg)
                    else:
                        return (
                            "Spell casting failed after max_attempts attempts"
                        )
            return "Spell casting failed after max_attempts attempts"

        return wrapper  # type: ignore[return-value]

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main():
    print(" Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f" Result: {result}")

    print("\n Testing retry spell...")

    @retry_spell(max_attempts=3)
    def waaaagh() -> str:
        raise Exception("Fizzle!")

    print(f" Result: {waaaagh()}")

    print("\n Testing MageGuild...")
    guild = MageGuild()
    print(f" {guild.validate_mage_name('Alex')}")
    print(f" {guild.validate_mage_name('Jo')}")
    print(f" {guild.cast_spell('Lightning', 15)}")
    print(f" {guild.cast_spell('Lightning', 5)}")


if __name__ == "__main__":
    main()
