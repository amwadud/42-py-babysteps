from pydantic import BaseModel, Field
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(None, max_length=200)


def main() -> None:
    print(" Space Station Data Validation ")
    print("========================================")

    valid_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2024, 1, 15, 10, 0, 0),
        is_operational=True,
        notes="Routine inspection completed",
    )

    print("\nValid station created:")
    print(f"  ID: {valid_station.station_id}")
    print(f"  Name: {valid_station.name}")
    print(f"  Crew: {valid_station.crew_size} people")
    print(f"  Power: {valid_station.power_level}%")
    print(f"  Oxygen: {valid_station.oxygen_level}%")
    status = (
        "Operational" if valid_station.is_operational else "Non-operational"
    )
    print(f"  Status: {status}")

    print("\n========================================")

    try:
        _ = SpaceStation(
            station_id="ISS001",
            name="Test Station",
            crew_size=25,
            power_level=85.0,
            oxygen_level=90.0,
            last_maintenance=datetime(2024, 1, 15, 10, 0, 0),
            notes=None,
        )
    except Exception as e:
        print("\nExpected validation error:")
        print(f"  {e}")


if __name__ == "__main__":
    main()
