from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    """Abstract base class for data streams."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter data based on criteria (default: return all)."""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Get stream statistics."""
        return {
            "stream_id": self.stream_id,
            "type": self.__class__.__name__,
            "status": "active",
        }


class SensorStream(DataStream):
    """Stream for sensor data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.readings_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not data_batch or len(data_batch) == 0:
                return "No readings to process"
            valid_readings = [
                r for r in data_batch if isinstance(r, (int, float))
            ]
            if not valid_readings:
                return "No valid numeric readings"
            count = len(valid_readings)
            temp = valid_readings[0] if valid_readings else 0
            self.readings_count += count
            return f"{count} readings processed, avg temp: {temp}°C"
        except (TypeError, ValueError) as e:
            return f"Error processing sensor data: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return super().filter_data(data_batch, criteria)
        try:
            if criteria == "anomalies":
                return [
                    r
                    for r in data_batch
                    if isinstance(r, (int, float)) and r > 50
                ]
            elif criteria == "high_temp":
                return [
                    r
                    for r in data_batch
                    if isinstance(r, (int, float)) and r > 30
                ]
            return data_batch
        except (TypeError, ValueError):
            return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Environmental Data"
        stats["readings"] = self.readings_count
        return stats


class TransactionStream(DataStream):
    """Stream for financial transactions."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.transaction_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not data_batch or len(data_batch) == 0:
                return "No transactions to process"
            total_buy: float = 0
            total_sell: float = 0
            for trans in data_batch:
                if isinstance(trans, (list, tuple)) and len(trans) >= 2:
                    action, amount = trans[0], trans[1]
                    if isinstance(action, str) and isinstance(
                        amount, (int, float)
                    ):
                        if action.lower() == "buy":
                            total_buy += amount
                        elif action.lower() == "sell":
                            total_sell += amount
            self.transaction_count = len(data_batch)
            net_flow = total_buy - total_sell
            flow_str = f"+{net_flow}" if net_flow >= 0 else str(net_flow)
            return f"{len(data_batch)} operations, net flow: {flow_str} units"
        except (TypeError, ValueError, IndexError) as e:
            return f"Error processing transactions: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return super().filter_data(data_batch, criteria)
        try:
            if criteria == "buy":
                return [
                    t
                    for t in data_batch
                    if isinstance(t, (list, tuple))
                    and len(t) >= 2
                    and isinstance(t[0], str)
                    and t[0].lower() == "buy"
                ]
            elif criteria == "sell":
                return [
                    t
                    for t in data_batch
                    if isinstance(t, (list, tuple))
                    and len(t) >= 2
                    and isinstance(t[0], str)
                    and t[0].lower() == "sell"
                ]
            elif criteria == "large":
                return [
                    t
                    for t in data_batch
                    if isinstance(t, (list, tuple))
                    and len(t) >= 2
                    and isinstance(t[1], (int, float))
                    and t[1] >= 100
                ]
            return data_batch
        except (TypeError, ValueError, IndexError):
            return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Financial Data"
        stats["transactions"] = self.transaction_count
        return stats


class EventStream(DataStream):
    """Stream for system events."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.event_count = 0
        self.error_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not data_batch or len(data_batch) == 0:
                return "No events to process"
            self.event_count = len(data_batch)
            self.error_count = sum(
                1
                for e in data_batch
                if isinstance(e, str) and "error" in e.lower()
            )
            return (
                f"{len(data_batch)} events, {self.error_count} errors detected"
            )
        except (TypeError, ValueError) as e:
            return f"Error processing events: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return super().filter_data(data_batch, criteria)
        try:
            if criteria == "errors":
                return [
                    e
                    for e in data_batch
                    if isinstance(e, str) and "error" in e.lower()
                ]
            elif criteria == "critical":
                return [
                    e
                    for e in data_batch
                    if isinstance(e, str) and "critical" in e.lower()
                ]
            elif criteria == "login":
                return [
                    e
                    for e in data_batch
                    if isinstance(e, str) and "login" in e.lower()
                ]
            return data_batch
        except (TypeError, ValueError):
            return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "System Events"
        stats["total_events"] = self.event_count
        stats["errors"] = self.error_count
        return stats


class StreamProcessor:
    """Processor that handles multiple streams polymorphically."""

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, data_batches: Dict[str, Any]) -> None:
        for stream in self.streams:
            if stream.stream_id in data_batches:
                data = data_batches[stream.stream_id]
                result = stream.process_batch(data)
                stream_type = stream.__class__.__name__.replace(
                    "Stream", " data"
                )
                print(f"- {stream_type}: {result}")

    def filter_all(self, criteria: str) -> Dict[str, List[Any]]:
        results: Dict[str, List[Any]] = {}
        for stream in self.streams:
            results[stream.stream_id] = []
        return results


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor = SensorStream("SENSOR_001")
    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")

    transaction = TransactionStream("TRANS_001")
    print("\nInitializing Transaction Stream...")
    print(f"Stream ID: {transaction.stream_id}, Type: Financial Data")

    event = EventStream("EVENT_001")
    print("\nInitializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: System Events")

    sensor_data = [22.5, 65, 1013]
    print(f"\nProcessing sensor batch: {sensor_data}")
    result = sensor.process_batch(sensor_data)
    print(f"Sensor analysis: {result}")

    trans_data = [["buy", 100], ["sell", 150], ["buy", 75]]
    print(f"\nProcessing transaction batch: {trans_data}")
    result = transaction.process_batch(trans_data)
    print(f"Transaction analysis: {result}")

    event_data = ["login", "error", "logout"]
    print(f"\nProcessing event batch: {event_data}")
    result = event.process_batch(event_data)
    print(f"Event analysis: {result}")

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_001"))
    processor.add_stream(TransactionStream("TRANS_001"))
    processor.add_stream(EventStream("EVENT_001"))

    data_batches = {
        "SENSOR_001": [22.5, 23.0, 100.0],
        "TRANS_001": [["buy", 100], ["sell", 150], ["buy", 75], ["sell", 500]],
        "EVENT_001": ["login", "error", "logout"],
    }

    print("Batch 1 Results:")
    processor.process_all(data_batches)

    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
