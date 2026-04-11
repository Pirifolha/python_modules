#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class ImproperError(Exception):
    def __init__(self, message="Got exception: Improper numeric data"):
        super().__init__(message)


class DataProcessor(ABC):

    def __init__(self):
        self.data = []
        self.counter = -1

    def output(self) -> tuple[int, str]:
        if len(self.data) == 0:
            raise IndexError("No data available")
        value = self.data[0]
        self.data.pop(0)
        self.counter += 1
        return self.counter, value

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> bool:
        pass


class NumericProcessor(DataProcessor):

    def validate(self, data):
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list) and all(
            isinstance(x, (int, float)) for x in data
        ):
            return True
        else:
            return False

    def ingest(self, data):
        if not self.validate(data):
            raise ImproperError("Got exception: Improper numeric data")

        print(f"Processing data: {data}")
        if isinstance(data, (int, float)):
            self.data = [str(data)]
        else:
            self.data = [str(x) for x in data]


class TextProcessor(DataProcessor):

    def validate(self, data):
        if isinstance(data, (str)):
            return True
        elif isinstance(data, list) and all(
            isinstance(x, (str)) for x in data
        ):
            return True
        else:
            return False

    def ingest(self, data):
        if not self.validate(data):
            raise ValueError("Got exception: Improper numeric data")

        print(f"Processing data: {data}")
        if isinstance(data, (str)):
            self.data = [data]
        else:
            self.data = [x for x in data]


class LogProcessor(DataProcessor):

    def validate(self, data):
        if isinstance(data, dict) and all(
            isinstance(k, (str)) and isinstance(v, (str))
            for k, v in data.items()
        ):
            return True
        if isinstance(data, list) and all(
            isinstance(d, dict)
            and all(
                isinstance(k, str) and isinstance(v, str) for k, v in d.items()
            )
            for d in data
        ):
            return True
        return False

    def ingest(self, data):
        if not self.validate(data):
            raise ValueError("Got exception: Improper log data")
        print(f"Processing data: {data}")
        if isinstance(data, dict):
            self.data = [f"{data['log_level']}: {data['log_message']}"]
        else:
            self.data = [f"{d['log_level']}: {d['log_message']}" for d in data]


def num_test():
    num = NumericProcessor()
    valid = 42
    invalid = "Hello"

    print("Testing Numeric Processor...")
    print(
        f"Trying to validate with input '{invalid}': {num.validate(invalid)}"
    )
    print(f"Trying to validate with input '{valid}': {num.validate(valid)}")
    # print(
    #     f"Test invalid ingestion of string {invalid} without prior valida
    # tion:"
    # )
    # num.ingest(invalid)
    num.ingest([23, 43, 60, 76, 95])
    print("Extracting 3 values...")
    for i in range(3):
        x, y = num.output()
        print(f"Numeric value {x}: {y}")


def text_test() -> None:
    text = TextProcessor()

    invalid = 42

    print("Testing Text Processor...")
    print(
        f"Trying to validate with input '{invalid}': {text.validate(invalid)}"
    )
    text.ingest(["hello", "world", "forty", "two"])
    print("Extracting 1 value...")
    x, y = text.output()
    print(f"Test value: {x}: {y}")


def log_test() -> None:
    log = LogProcessor()
    invalid = "Hello"

    print("Testing Log Processor...")
    print(
        f"Trying to validate with input '{invalid}': {log.validate(invalid)}"
    )
    log.ingest(
        [
            {"log_level": "NOTICE", "log_message": "Connection to server"},
            {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
        ]
    )

    print("Extracting 2 values...")
    for i in range(2):
        x, y = log.output()
        print(f"Numeric value {x}: {y}")


if __name__ == "__main__":
    num_test()
    print("\n")
    text_test()
    print("\n")
    log_test()
