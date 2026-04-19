from ex1.factory import HealingCreatureFactory, TransformCreatureFactory


def test_healing(factory: HealingCreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())  # type: ignore[attr-defined]
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())  # type: ignore[attr-defined]


def test_transform(factory: TransformCreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())  # type: ignore[attr-defined]
    print(base.attack())
    print(base.revert())  # type: ignore[attr-defined]
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())  # type: ignore[attr-defined]
    print(evolved.attack())
    print(evolved.revert())  # type: ignore[attr-defined]


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    hcf = HealingCreatureFactory()
    test_healing(hcf)
    print()
    print("Testing Creature with transform capability")
    tcf = TransformCreatureFactory()
    test_transform(tcf)
