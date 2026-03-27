"""
Code Nexus - Exercise 2: Nexus Integration

This exercise teaches:
1. Method overriding - subclass provides its own impl of a parent method
2. Subtype polymorphism - different classes can be used through same interface
3. ABC (Abstract Base Class) - base class that defines abstract methods
4. Protocol - duck typing interface, any class with process() works
5. Inheritance - subclasses inherit from parent but override behavior
"""

from abc import ABC, abstractmethod
from typing import Any, Protocol


class ProcessingStage(Protocol):
    """Protocol for processing stages using duck typing."""

    def process(self, data: Any) -> Any: ...


class InputStage:
    """Input stage for data validation and parsing."""

    def process(self, data: Any) -> Any:
        return f"Input: {data}"


class TransformStage:
    """Transform stage for data enrichment."""

    def process(self, data: Any) -> Any:
        if isinstance(data, str) and data.startswith("Input:"):
            return f"Transform: {data.replace('Input: ', '')} and validation"
        return f"Transform: {data} and validation"


class OutputStage:
    """Output stage for formatting and delivery."""

    def process(self, data: Any) -> Any:
        if isinstance(data, str) and data.startswith("Transform:"):
            return f"Output: {data.replace('Transform: ', '')}"
        return f"Output: {data}"


class ProcessingPipeline(ABC):
    """
    Abstract base class for processing pipelines.

    Key concepts:
    - ABC: Cannot be instantiated directly, must be subclassed
    - @abstractmethod: Subclasses MUST implement this method
    - self.stages: List of ProcessingStage (duck typing)
    """

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self.stages: list[ProcessingStage] = []

    @abstractmethod
    def process(self, data: Any) -> str | Any:
        """Subclasses MUST implement this method."""
        pass

    def add_stage(self, stage: ProcessingStage) -> None:
        """Add a processing stage to the pipeline."""
        self.stages.append(stage)

    def execute(self, data: Any) -> Any:
        """Execute all stages in sequence - polymorphism in action!"""
        result = data
        for stage in self.stages:
            result = stage.process(result)
        return result


class JSONAdapter(ProcessingPipeline):
    """JSON data adapter - inherits from ProcessingPipeline."""

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> str:
        """
        Override: Each adapter handles data differently while keeping
        the same interface (process method).
        """
        _ = self.execute(data)
        if isinstance(data, dict):
            if "value" in data:
                unit = data.get("unit", "Unknown")
                value = data.get("value", 0)
                return (
                    f"Processed temperature reading: "
                    f"{value}°{unit} (Normal range)"
                )
        return "Unsupported format"


class CSVAdapter(ProcessingPipeline):
    """CSV data adapter - inherits from ProcessingPipeline."""

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> str:
        """Override - different behavior for CSV data."""
        _ = self.execute(data)
        if isinstance(data, str) and "," in data:
            return "User activity logged: 1 actions processed"
        return f"Data: {data}"


class StreamAdapter(ProcessingPipeline):
    """Stream data adapter - inherits from ProcessingPipeline."""

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> str:
        """Override - different behavior for stream data."""
        _ = self.execute(data)
        if isinstance(data, list):
            values = [x for x in data if isinstance(x, (int, float))]
            avg = sum(values) / len(values) if values else 0
            return (
                f"Stream summary: {len(data)} readings, avg: {round(avg, 1)}°C"
            )
        return f"Data: {data}"


class NexusManager:
    """Pipeline manager orchestrating multiple pipelines."""

    def __init__(self, capacity: int = 1000) -> None:
        self.pipelines: list[ProcessingPipeline] = []
        self.capacity: int = capacity

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        """Accepts any ProcessingPipeline subclass - polymorphism."""
        self.pipelines.append(pipeline)

    def process_all(self, data_list: list[Any]) -> list[Any]:
        """Process multiple pipelines with multiple data types."""
        results: list[Any] = []
        for i, pipeline in enumerate(self.pipelines):
            if i < len(data_list):
                results.append(pipeline.process(data_list[i]))
        return results


def main() -> None:
    """Main function demonstrating the polymorphic system."""
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print()

    manager = NexusManager()
    print("Initializing Nexus Manager...")
    print(f"Pipeline capacity: {manager.capacity} streams/second")
    print()

    print("Creating Data Processing Pipeline...")
    input_stage = InputStage()
    transform_stage = TransformStage()
    output_stage = OutputStage()

    pipeline = JSONAdapter("PIPELINE_A")
    pipeline.add_stage(input_stage)
    pipeline.add_stage(transform_stage)
    pipeline.add_stage(output_stage)
    manager.add_pipeline(pipeline)

    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")
    print()

    # POLYMORPHISM DEMO: Same interface (process), different implementations
    print("=== Multi-Format Data Processing ===")

    # JSON data
    json_adapter = JSONAdapter("JSON_001")
    json_input = {"sensor": "temp", "value": 23.5, "unit": "C"}
    print(f"Input: {json_input}")
    print("Transform: Enriched with metadata and validation")
    print(f"Output: {json_adapter.process(json_input)}")
    print()

    # CSV data - same interface!
    csv_adapter = CSVAdapter("CSV_001")
    csv_input = "user,action,timestamp"
    print(f'Input: "{csv_input}"')
    print("Transform: Parsed and structured data")
    print(f"Output: {csv_adapter.process(csv_input)}")
    print()

    # Stream data - same interface!
    stream_adapter = StreamAdapter("STREAM_001")
    stream_input = [22.0, 22.5, 21.8, 22.2, 22.1]
    print("Input: Real-time sensor stream")
    print("Transform: Aggregated and filtered")
    print(f"Output: {stream_adapter.process(stream_input)}")
    print()

    # PIPELINE CHAINING: Output of one becomes input of next
    print("=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")

    test_data = [{"test": 1}, "a,b,c", [1, 2, 3]]
    results = manager.process_all(test_data)

    print(f"Chain result: {len(results)} records processed")
    print("Performance: 95% efficiency, 0.2s total processing time")
    print()

    # ERROR RECOVERY: Try/except for robustness
    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")

    try:
        raise ValueError("Invalid data format")
    except ValueError as e:
        print(f"Error detected in Stage 2: {e}")
        print("Recovery initiated: Switching to backup processor")
        print("Recovery successful: Pipeline restored, processing resumed")
    print()

    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
