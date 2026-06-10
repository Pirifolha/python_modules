#!/usr/bin/env python3

from datetime import datetime

try:
    from pydantic import BaseModel, Field, ValidationError  # type: ignore
except ModuleNotFoundError:
    print(
        "\nError! Missing module: pydantic\n",
        "Create a venv, activate it and install the ",
        'module using: pip install "pydantic>=2.0"\n\n',
        "Exiting.",
        sep="",
    )
    exit()


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0, description="Oxygen")
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(max_length=200)


def main() -> None:
    valid_station = SpaceStation(
        station_id="ISS001",
        name="International space station",
        crew_size=6,
        power_level=72.3,
        oxygen_level=92.4,
        last_maintenance=datetime.now(),
        is_operational=True,
        notes="Station successfully created!",
    )

    print("Space Station Data Validation")
    print("=====================================")
    print("Valid station created")
    print(f"ID: {valid_station.station_id}")
    print(f"Name: {valid_station.name}")
    print(f"Crew: {valid_station.crew_size} people")
    print(f"Power: {valid_station.power_level}%")
    print(f"Oxygen: {valid_station.oxygen_level}%")
    print("Status: Operational")

    print("\n========================================")
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="ISS001",
            name="International space station",
            crew_size=26,
            power_level=72.3,
            oxygen_level=92.4,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes="Station successfully created!",
        )
    except ValidationError as error:
        for issue in error.errors():
            print(issue["msg"])


if __name__ == "__main__":
    main()
