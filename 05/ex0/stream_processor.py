#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: list[Any] | tuple[Any] | int | float) -> str:
        try:
            if isinstance(data, (list, tuple)):
                numbers = [
                    float(x) for x in data if isinstance(x, (int, float))
                ]
                if numbers:
                    total = sum(numbers)
                    return self.format_output(
                        f"Processed {len(numbers)} numeric values, "
                        f"sum={int(total)}, avg={total / len(numbers)}"
                    )
                return self.format_output("No numeric values found")
            return self.format_output(str(float(data)))
        except ValueError as e:
            return self.format_output(f"Invalid numeric value: {e}")
        except TypeError as e:
            return self.format_output(f"Unsupported data type: {e}")
        except OverflowError as e:
            return self.format_output(f"Number too large: {e}")

    def validate(self, data: list[Any] | tuple[Any] | int | float) -> bool:
        if isinstance(data, (list, tuple)):
            for x in data:
                if not isinstance(x, (int, float)):
                    return False
        return isinstance(data, (int, float))


class TextProcessor(DataProcessor):
    def process(self, data: str) -> str:
        if isinstance(data, str):
            words_count = len(data.split())
            chars_count = len(data)
            return self.format_output(
                f"Processed text: {chars_count} characters, "
                f"{words_count} words"
            )

    def validate(self, data: str) -> bool:
        if isinstance(data, str):
            return True
        return False


class LogProcessor(DataProcessor):
    def validate(self, data: str) -> bool:
        return isinstance(data, str) and len(data.strip()) > 0 and ":" in data

    def process(self, data: str) -> str:
        if not self.validate(data):
            return self.format_output("Error: Invalid log data")
        log_levels = ["ERROR", "WARNING", "INFO", "DEBUG", "CRITICAL"]

        data_upper = data.upper()
        detected_level = "INFO"
        for level in log_levels:
            if level in data_upper:
                detected_level = level
                break

        message = data.split(":", 1)[1].strip()
        prefix = (
            "[ALERT]"
            if detected_level in ("ERROR", "CRITICAL")
            else f"[{detected_level}]"
        )

        return self.format_output(
            f"{prefix} {detected_level} level detected: {message}"
        )


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    numeric = NumericProcessor()
    print("Initializing Numeric Processor...")
    numeric_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    print(numeric.process(numeric_data))
    print()

    text = TextProcessor()
    print("Initializing Text Processor...")
    text_data = "Hello Nexus World"
    print(f'Processing data: "{text_data}"')
    print(text.process(text_data))
    print()

    log = LogProcessor()
    print("Initializing Log Processor...")
    log_data = "ERROR: Connection timeout"
    print(f'Processing data: "{log_data}"')
    print(log.process(log_data))
    print()

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...\n")

    processor_data_combos: tuple[tuple[DataProcessor, Any], ...] = (
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "Hello World"),
        (LogProcessor(), "INFO: System ready"),
    )

    for i, (proc, data) in enumerate(processor_data_combos, 1):
        result = proc.process(data)
        print(f"Result {i}: {result.split(':', 1)[1].strip()}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
