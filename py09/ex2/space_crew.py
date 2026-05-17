#!/usr/bin/env python3

from pydantic import BaseModel, Field, model_validator
from enum import Enum
from datetime import datetime


class Rank(Enum):
    cadet = 1
    officer = 2
    lieutenant = 3
    captain = 4
    commander = 5


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def requirements(self):
        if self.mission_id[0] != "M":
            raise ValueError("Mission ID must start with 'M'")

        has_superior = False
        for member in self.crew:
            if (
                member.rank == Rank.commander
                or member.rank == Rank.captain
            ):
                has_superior = True

        if has_superior is False:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced: int = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced += 1

            if (experienced / len(self.crew) * 100) < 50:
                raise ValueError(
                    "Long mission (> 365 days) need 50% experienced crew (5+ years)"
                )

        for member in self.crew:
            if member.is_active is False:
                raise ValueError("All crew members must be active")

        return self


def main():
    print("Space Mission Crew Validation")
    print("============================================")

    member1 = CrewMember(
        member_id="Id_1234",
        name="Sarah Connor",
        rank=5,
        age=38,
        specialization="Mission Command",
        years_experience=12,
    )

    member2 = CrewMember(
        member_id="Id_9384",
        name="John Smith",
        rank=3,
        age=32,
        specialization="Navigation",
        years_experience=7,
    )

    member3 = CrewMember(
        member_id="Id_5678",
        name="Alice Johnson",
        rank=2,
        age=28,
        specialization="Engineering",
        years_experience=6,
    )

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.now(),
        duration_days=900,
        crew=[member1, member2, member3],
        budget_millions=2500.0,
    )

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")

    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.name}) - {member.specialization}"
        )

    print("============================================")
    print("Expected validation error:")

    try:
        invalid_member = CrewMember(
            member_id="Id_9999",
            name="Mark Davis",
            rank=2,
            age=40,
            specialization="Science",
            years_experience=10,
        )

        SpaceMission(
            mission_id="M2025_TEST",
            mission_name="Test Mission",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=30,
            crew=[invalid_member],
            budget_millions=100.0,
        )

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
