#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any
from typing import Protocol


class ImproperError(Exception):
    def __init__(self, message="Got exception: Improper numeric data"):
        super().__init__(message)


class DataStreamError(Exception):
    def __init__(self, message="Data stream error:"):
        super().__init__(message)


class DataProcessor(ABC):

    def __init__(self):
        self.data = []
        self.counter = -1
        self.total_processed = 0

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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        values = [value for _, value in data]
        line = ",".join(values)
        print(line)


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        pairs = []
        for index, value in data:
            pairs.append(f'"item_{index}:" "{value}"')
        content = ", ".join(pairs)
        json_str = "{" + content + "}"
        print(json_str)


class DataStream:

    def __init__(self):
        self.processors = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            found = False
            for proc in self.processors:
                if proc.validate(data):
                    proc.ingest(data)
                    found = True
                    break
            if not found:
                print(
                    f"DataStream error - Can't process element in "
                    f"stream: {data}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self.processors) == 0:
            print("No processor found, no data")
            return
        for proc in self.processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            print(
                f"{name}: Total {proc.total_processed} items processed, "
                f"remaining {len(proc.data)} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            collected = []
            for _ in range(nb):
                try:
                    res = proc.output()
                    collected.append(res)
                except IndexError:
                    break
            if collected:
                plugin.process_output(collected)


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

        if isinstance(data, (int, float)):
            self.data.append(str(data))
            self.total_processed += 1
        else:
            for x in data:
                self.data.append(str(x))
                self.total_processed += 1


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

        if isinstance(data, (str)):
            self.data.append(data)
            self.total_processed += 1
        else:
            for x in data:
                self.data.append(x)
                self.total_processed += 1


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

        if isinstance(data, dict):
            self.data.append(f"{data['log_level']}: {data['log_message']}")
            self.total_processed += 1
        else:
            for d in data:
                self.data.append(f"{d['log_level']}: {d['log_message']}")
                self.total_processed += 1


def main():
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...\n")
    ds = DataStream()

    ds.print_processors_stats()

    print("\nRegistering Processors\n")
    ds.register_processor(NumericProcessor())
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    stream = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print("Send the first batch of data on stream", stream, "\n")
    ds.process_stream(stream)

    ds.print_processors_stats()
    print("")

    print("Send 3 processed data from each processor to a CSV plugin")
    ds.output_pipeline(3, CSVPlugin())
    print("")

    sec_stream = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print("Send the first batch of data on stream", sec_stream)
    ds.process_stream(sec_stream)

    print("")
    ds.print_processors_stats()
    print("")

    print("Send 5 processed data from each processor to a JSON plugin")
    ds.output_pipeline(5, JSONPlugin())
    print("")

    ds.print_processors_stats()
    print("")


if __name__ == "__main__":
    main()
