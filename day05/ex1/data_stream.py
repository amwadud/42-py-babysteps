from abc import ABC, abstractmethod
from typing import Any


class DataStream(ABC):
    """Abstract base class for all stream types."""

    def __init__(self, stream_id: str) -> None:
        """Initialize the data stream with an identifier.

        Args:
            stream_id: Unique identifier for this stream.
        """
        self.stream_id: str = stream_id

    @abstractmethod
    def process_batch(self, data_batch: list[Any]) -> str:
        """Process data and return result string.

        Args:
            data_batch: List of data items to process.

        Returns:
            A string describing the processing results.
        """
        pass

    def filter_data(
        self, data_batch: list[Any], criteria: str | None = None
    ) -> list[Any]:
        """Filter data based on criteria.

        Args:
            data_batch: List of data items to filter.
            criteria: Optional filter criteria string.

        Returns:
            Filtered list of data items.
        """
        return data_batch

    def get_stats(self) -> dict[str, Any]:
        """Return stream statistics.

        Returns:
            Dictionary containing stream statistics.
        """
        return {"stream_id": self.stream_id, "processed": 0}


class SensorStream(DataStream):
    """Process sensor/temperature data."""

    def process_batch(self, data_batch: list[Any]) -> str:
        """Process temperature sensor data and calculate average.

        Args:
            data_batch: List of sensor data dictionaries with 'temp' keys.

        Returns:
            String describing processing results
            with count and average temperature.
        """
        temps: list[float] = []
        count: int = len(data_batch)
        for d in data_batch:
            if "temp" in d:
                temps.append(d["temp"])
        avg: float = sum(temps) / len(temps) if temps else 0
        return (
            f"Sensor analysis: {count} readings processed, avg temp: {avg}°C"
        )

    def filter_data(
        self, data_batch: list[Any], criteria: str | None = None
    ) -> list[Any]:
        """Filter sensor data by priority level.

        Args:
            data_batch: List of sensor data items.
            criteria: Filter criteria - 'high-priority' returns temps > 20.

        Returns:
            Filtered list of sensor data.
        """
        if criteria == "high-priority":
            return [
                d for d in data_batch if "temp" in d and d.get("temp", 0) > 20
            ]
        return data_batch


class TransactionStream(DataStream):
    """Process financial transaction data."""

    def process_batch(self, data_batch: list[Any]) -> str:
        """Process financial transactions and calculate net flow.

        Args:
            data_batch: List of transaction dictionaries
            with 'buy' or 'sell' keys.

        Returns:
            String describing transaction processing results with net flow.
        """
        net: int = 0
        for t in data_batch:
            if "buy" in t:
                net += t["buy"]
            if "sell" in t:
                net -= t["sell"]
        return (
            f"Transaction analysis: {len(data_batch)} operations, "
            f"net flow: {net:+d} units"
        )

    def filter_data(
        self, data_batch: list[Any], criteria: str | None = None
    ) -> list[Any]:
        """Filter transactions by size.

        Args:
            data_batch: List of transaction data items.
            criteria: Filter criteria - 'large' returns transactions > 100.

        Returns:
            Filtered list of transactions.
        """
        if criteria == "large":
            return [
                d
                for d in data_batch
                if ("buy" in d and d["buy"] > 100)
                or ("sell" in d and d["sell"] > 100)
            ]
        return data_batch


class EventStream(DataStream):
    """Process system event data."""

    def process_batch(self, data_batch: list[Any]) -> str:
        """Process system events and count errors.

        Args:
            data_batch: List of event strings.

        Returns:
            String describing event processing with error count.
        """
        errors: int = 0
        for e in data_batch:
            if e == "error":
                errors += 1
        return (
            f"Event analysis: {len(data_batch)} events, "
            f"{errors} errors detected"
        )


class StreamProcessor:
    """Manages multiple streams and processes them polymorphically."""

    def __init__(self) -> None:
        """Initialize the stream processor with an empty stream list."""
        self.streams: list[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Add a data stream to the processor.

        Args:
            stream: DataStream instance to add.
        """
        self.streams.append(stream)

    def process_all(self, batches: list[list[Any]]) -> list[str]:
        """Process all streams with their corresponding data batches.

        Args:
            batches: List of data batches, one per stream.

        Returns:
            List of result strings from processing each stream.
        """
        results: list[str] = []
        for i in range(len(self.streams)):
            if i < len(batches):
                # Polymorphism: same method call, different behavior
                results.append(self.streams[i].process_batch(batches[i]))
        return results


def main() -> None:
    """Run the polymorphic stream processing demonstration."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    data: dict[str, dict[str, Any]] = {
        "sensor": {
            "type": "Environmental Data",
            "var": SensorStream("SENSOR_001"),
            "batch": [{"temp": 22.5, "humidity": 65, "pressure": 1013}],
        },
        "trans": {
            "type": "Financial Data",
            "var": TransactionStream("TRANS_001"),
            "batch": [{"buy": 100}, {"sell": 150}, {"buy": 75}],
        },
        "event": {
            "type": "System Events",
            "var": EventStream("EVENT_001"),
            "batch": ["login", "error", "logout"],
        },
    }

    sensor: SensorStream = data["sensor"]["var"]
    sensor_batch = data["sensor"]["batch"]
    print(
        "Initializing Sensor Stream... \n" +
        f"Stream ID: {sensor.stream_id}, Type: {data['sensor']['type']},\n" +
        f"Processing sensor batch: {sensor_batch}, \n" +
        f"{sensor.process_batch(sensor_batch)}\n"
    )

    trans: TransactionStream = data["trans"]["var"]
    trans_batch = data["trans"]["batch"]
    print(
        "Initializing Transaction Stream... \n" +
        f"Stream ID: {trans.stream_id}, Type: {data['trans']['type']}\n" +
        f"Processing transaction batch: {trans_batch}\n" +
        f"{trans.process_batch(trans_batch)}\n"
    )

    event: EventStream = data["event"]["var"]
    event_batch = data["event"]["batch"]
    print(
        "Initializing Event Stream...\n" +
        f"Stream ID: {event.stream_id}, Type: {data['event']['type']}\n" +
        f"Processing event batch: {event_batch}\n" +
        f"{event.process_batch(event_batch)}\n"
    )

    print(
        "=== Polymorphic Stream Processing ===\n" +
        "    Processing mixed stream types through unified interface...\n"
    )

    # Polymorphism: same interface, different implementations
    processor: StreamProcessor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)

    batches: list[list[Any]] = [
        [{"temp": 22.5}, {"temp": 28.0}],
        [{"buy": 100}, {"sell": 200}, {"buy": 50}, {"sell": 80}],
        ["login", "error", "logout"],
    ]
    processor.process_all(batches)

    print(
        "Batch 1 Results:\n"
        + f"- Sensor data: {len(batches[0])} readings processed\n"
        + f"- Transaction data: {len(batches[1])} operations processed\n"
        + f"- Event data: {len(batches[2])} events processed\n"
    )

    print("Stream filtering active: High-priority data only")
    filtered_sensor: list[Any] = sensor.filter_data(
        batches[0], "high-priority"
    )
    filtered_trans: list[Any] = trans.filter_data(batches[1], "large")
    print(
        f"Filtered results: {len(filtered_sensor)} critical sensor alerts, " +
        f"{len(filtered_trans)} large transaction\n"
    )

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
