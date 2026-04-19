from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)
from ex2.strategy import BattleStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    n = len(opponents)
    print(f" *** Tournament ***\n {n} opponents involved")

    for i in range(n):
        for j in range(i + 1, n):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print("\n * Battle *")
            print(f" {creature1.describe()}")
            print("  vs.")
            print(f" {creature2.describe()}")
            print("  now fight!")

            try:
                strategy1.act(creature1)
            except InvalidStrategyError as e:
                print(f"  Battle error, aborting tournament: {e}")
                return

            try:
                strategy2.act(creature2)
            except InvalidStrategyError as e:
                print(f"  Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    ff = FlameFactory()
    af = AquaFactory()
    hcf = HealingCreatureFactory()
    tcf = TransformCreatureFactory()

    ns = NormalStrategy()
    ags = AggressiveStrategy()
    ds = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(ff, ns), (hcf, ds)])

    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(ff, ags), (hcf, ds)])

    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(af, ns), (hcf, ds), (tcf, ags)])
