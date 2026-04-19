from ex0 import FlameFactory, AquaFactory


def test_factory(factory: FlameFactory | AquaFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle(f1: FlameFactory, f2: AquaFactory) -> None:
    base1 = f1.create_base()
    base2 = f2.create_base()
    print(f"{base1.describe()}")
    print(" vs.\n")
    print(f"{base2.describe()}")
    print(" fight!")
    print(base1.attack())
    print(base2.attack())


if __name__ == "__main__":
    print("Testing factory")
    ff = FlameFactory()
    af = AquaFactory()
    test_factory(ff)
    print()
    print("Testing factory")
    test_factory(af)
    print()
    print("Testing battle")
    battle(ff, af)
