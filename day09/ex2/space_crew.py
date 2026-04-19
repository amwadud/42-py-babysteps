from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from enum import Enum


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_commander_or_captain = any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        )
        if not has_commander_or_captain:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced_count = sum(
                1 for member in self.crew if member.years_experience >= 5
            )
            required_experienced = len(self.crew) / 2
            if experienced_count < required_experienced:
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced "
                    + "crew (5+ years)"
                )

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print(" Space Mission Crew Validation ")
    print("========================================")

    valid_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2025, 3, 15, 8, 0, 0),
        duration_days=900,
        crew=[
            CrewMember(
                member_id="M001",
                name="Sarah Connor",
                rank=Rank.COMMANDER,
                age=38,
                specialization="Mission Command",
                years_experience=15,
                is_active=True,
            ),
            CrewMember(
                member_id="M002",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=32,
                specialization="Navigation",
                years_experience=8,
                is_active=True,
            ),
            CrewMember(
                member_id="M003",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=28,
                specialization="Engineering",
                years_experience=5,
                is_active=True,
            ),
        ],
        mission_status="planned",
        budget_millions=2500.0,
    )

    print("\nValid mission created:")
    print(f"  Mission: {valid_mission.mission_name}")
    print(f"  ID: {valid_mission.mission_id}")
    print(f"  Destination: {valid_mission.destination}")
    print(f"  Duration: {valid_mission.duration_days} days")
    print(f"  Budget: ${valid_mission.budget_millions}M")
    print(f"  Crew size: {len(valid_mission.crew)}")
    print("  Crew members:")
    for member in valid_mission.crew:
        rank = member.rank.value
        print(f"    - {member.name} ({rank}) - {member.specialization}")

    print("\n========================================")

    try:
        _ = SpaceMission(
            mission_id="M2024_TEST",
            mission_name="Test Mission",
            destination="Moon",
            launch_date=datetime(2025, 1, 1, 0, 0, 0),
            duration_days=30,
            crew=[
                CrewMember(
                    member_id="T001",
                    name="Test Person",
                    rank=Rank.OFFICER,
                    age=25,
                    specialization="Test",
                    years_experience=1,
                    is_active=True,
                )
            ],
            mission_status="planned",
            budget_millions=100.0,
        )
    except Exception as e:
        print("\nExpected validation error:")
        print(f"  {e}")


if __name__ == "__main__":
    main()
