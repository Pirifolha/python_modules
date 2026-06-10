#!/usr/bin/env python3

from enum import Enum
from datetime import datetime

try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ModuleNotFoundError:
    print(
        "\nError! Missing module: pydantic\n",
        "Create a venv, activate it and install the ",
        'module using: pip install "pydantic>=2.0"\n\n',
        "Exiting.",
        sep="",
    )
    exit()


class ContactType(Enum):
    radio = 1
    visual = 2
    physical = 3
    telepathic = 4


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def checks(self):
        if self.contact_id[:2] != "AC":
            raise ValueError("Contact id must start with 'AC'")
        if self.contact_type == ContactType.physical:
            if self.is_verified is False:
                raise ValueError("Physical contact reports must be verfied")
        if self.contact_type == ContactType.telepathic:
            if self.witness_count < 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses"
                )
        if self.signal_strength > 7.0:
            if not self.message_received:
                raise ValueError("Strong signals should include messages")
        return self


valid_alien = AlienContact(
    contact_id="AC_2024_001",
    timestamp=datetime.now(),
    location="Area 51, Nevada",
    contact_type=ContactType.radio,
    signal_strength=8.5,
    duration_minutes=45,
    witness_count=5,
    message_received="Greetings from Zeta Reticuli",
)


def main():

    print("Alien Contact Log Validation")
    print("===================================")
    print("Valid contact report:")
    print(f"ID: {valid_alien.contact_id}")
    print(f"Type: {valid_alien.contact_type.name}")
    print(f"Location: {valid_alien.location}")
    print(f"Signal: {valid_alien.signal_strength}/10")
    print(f"Duration: {valid_alien.duration_minutes} minutes")
    print(f"Witnesses: {valid_alien.duration_minutes}")
    print(f"Message: {valid_alien.message_received}")

    print("\n===================================")
    print("Expected validiton error:")
    try:
        AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
        )

    except ValidationError as error:
        for issue in error.errors():
            print(issue["msg"])


if __name__ == "__main__":
    main()
