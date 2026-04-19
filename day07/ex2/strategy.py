from abc import ABC, abstractmethod

from ex0.creature import Creature


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None: ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool: ...


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        print(f" {creature.attack()}")

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for "
                "this aggressive strategy"
            )
        print(f" {creature.transform()}")  # type: ignore[attr-defined]
        print(f" {creature.attack()}")
        print(f" {creature.revert()}")  # type: ignore[attr-defined]

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "transform") and hasattr(creature, "revert")


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for "
                "this defensive strategy"
            )
        print(f" {creature.attack()}")
        print(f" {creature.heal()}")  # type: ignore[attr-defined]

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "heal")
