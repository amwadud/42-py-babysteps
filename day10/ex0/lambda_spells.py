from typing import TypedDict


class Artifact(TypedDict):
    name: str
    power: int
    type: str


class Mage(TypedDict):
    name: str
    power: int
    element: str


class MageStats(TypedDict):
    max_power: int
    min_power: int
    avg_power: float


def artifact_sorter(artifacts: list[Artifact]) -> list[Artifact]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[Mage], min_power: int) -> list[Mage]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[Mage]) -> MageStats:
    powers = [m["power"] for m in mages]
    return MageStats(
        max_power=max(powers),
        min_power=min(powers),
        avg_power=round(sum(powers) / len(powers), 2),
    )


if __name__ == "__main__":
    print("Testing artifact sorter...")
    artifacts: list[Artifact] = [
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    first = sorted_artifacts[0]
    second = sorted_artifacts[1]
    print(
        f"{first['name']} ({first['power']} power) "
        + "comes before "
        + f"{second['name']} ({second['power']} power)"
    )
    print()

    print("Testing spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print(" ".join(transformed))
