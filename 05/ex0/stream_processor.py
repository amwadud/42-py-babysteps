from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Abstract base class for data processors."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process data and return result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Format output string (default: return as-is)."""
        return result


class NumericProcessor(DataProcessor):
    """Processor for numeric data (lists of numbers)."""

    def validate(self, data: Any) -> bool:
        try:
            return (
                isinstance(data, list)
                and len(data) > 0
                and all(isinstance(item, (int, float)) for item in data)
            )
        except (TypeError, KeyError):
            return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                return "Error: Invalid numeric data"
            count = len(data)
            total = sum(data)
            average = total / count if count > 0 else 0
            return (
                f"Processed {count} numeric values, sum={total}, avg={average}"
            )
        except (TypeError, ZeroDivisionError) as e:
            return f"Error processing numeric data: {e}"


class TextProcessor(DataProcessor):
    """Processor for text data (strings)."""

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and len(data.strip()) > 0

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                return "Error: Invalid text data"
            char_count = len(data)
            word_count = len(data.split())
            return (
                f"Processed text: {char_count} characters, {word_count} words"
            )
        except (TypeError, AttributeError) as e:
            return f"Error processing text data: {e}"


class LogProcessor(DataProcessor):
    """Processor for log entries."""

    def __init__(self) -> None:
        super().__init__()
        self._log_levels = ["ERROR", "WARNING", "INFO", "DEBUG", "CRITICAL"]

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and len(data.strip()) > 0 and ":" in data

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                return "Error: Invalid log data"
            data_upper = data.upper()
            detected_level = "INFO"
            for level in self._log_levels:
                if level in data_upper:
                    detected_level = level
                    break
            message = data
            if ":" in data:
                message = data.split(":", 1)[1].strip()
            if detected_level in ("ERROR", "CRITICAL"):
                return f"[ALERT] {detected_level} level detected: {message}"
            return f"[{detected_level}] {detected_level} level detected: {message}"
        except (TypeError, AttributeError) as e:
            return f"Error processing log data: {e}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    numeric = NumericProcessor()
    print("\nInitializing Numeric Processor...")
    numeric_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    if numeric.validate(numeric_data):
        print("Validation: Numeric data verified")
    result = numeric.process(numeric_data)
    print(f"Output: {result}")

    text = TextProcessor()
    print("\nInitializing Text Processor...")
    text_data = "Hello Nexus World"
    print(f'Processing data: "{text_data}"')
    if text.validate(text_data):
        print("Validation: Text data verified")
    result = text.process(text_data)
    print(f"Output: {result}")

    log = LogProcessor()
    print("\nInitializing Log Processor...")
    log_data = "ERROR: Connection timeout"
    print(f'Processing data: "{log_data}"')
    if log.validate(log_data):
        print("Validation: Log entry verified")
    result = log.process(log_data)
    print(f"Output: {result}")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors = [
        (numeric, [1, 2, 3]),
        (text, "Hello Nexus"),
        (log, "INFO: System ready"),
    ]

    for i, (processor, data) in enumerate(processors, 1):
        result = processor.process(data)
        print(f"Result {i}: {result}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")
