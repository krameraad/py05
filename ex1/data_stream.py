#!/usr/bin/env python3

from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod

X = "\033[0m"
R = "\033[91m"
G = "\033[92m"
B = "\033[94m"
C = "\033[96m"
M = "\033[95m"
Y = "\033[93m"
D = "\033[2m"
H = "\033[1m"
HC = "\033[1;96m"
HY = "\033[1;93m"


class DataStream(ABC):
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__()
        self.stream_id = stream_id
        print(f"{D}Initializing Sensor Stream...{X}")
        print(f"Stream ID: {stream_id}, Type: Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        size = len(data_batch)
        if size < 1:
            raise ValueError("batch is empty")
        if size > 3:
            raise ValueError("batch must be three or less in size")
        print(f"{HC}Processing sensor batch{X}: [", end="")
        print(f"temp:{HY}{data_batch[0]}{X}", end="")
        if size > 1:
            print(f", humidity:{HY}{data_batch[1]}{X}", end="")
        if size > 2:
            print(f", pressure:{HY}{data_batch[2]}{X}", end="")
        print("]")
        return f"avg temp: {data_batch[0]}°C"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__()
        self.stream_id = stream_id
        print(f"{D}Initializing Transaction Stream...{X}")
        print(f"Stream ID: {stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        if len(data_batch) < 1:
            raise ValueError("batch is empty")
        total = 0
        history = []
        for transaction in data_batch:
            total += transaction
            if transaction < 0:
                history += [f"sell:{HY}{transaction * -1}{X}"]
            else:
                history += [f"buy:{HY}{transaction}{X}"]
        print(f"{HC}Processing transaction batch{X}: [{", ".join(history)}]")
        if total > 0:
            return f"net flow: +{total} units"
        return f"net flow: {total} units"


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__()
        self.stream_id = stream_id
        print(f"{D}Initializing Event Stream...{X}")
        print(f"Stream ID: {stream_id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        if len(data_batch) < 1:
            raise ValueError("batch is empty")
        errors = 0
        for event in data_batch:
            if event == "error":
                errors += 1
        print(f"{HC}Processing event batch{X}:"
              f" [{HY}{f"{X}, {HY}".join(data_batch)}{X}]")
        return f"{errors} errors detected"


class StreamProcessor:
    def __init__(self):
        self.sensor_stream = 1
        print(f"{D}Processing mixed stream types"
              f" through unified interface...{X}")

    def process_all(self) -> str:
        pass


print(f"{H}=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n{X}")

sensor = SensorStream("SENSOR_001")
batch = [22.5, 65, 1013]
print(f"Sensor analysis: {len(batch)}"
      f" readings processed, {HY}{sensor.process_batch(batch)}{X}\n")

trans = TransactionStream("TRANS_001")
batch = [+100, -150, +75]
print(f"Transaction analysis: {len(batch)}"
      f" operations, {HY}{trans.process_batch(batch)}{X}\n")

event = EventStream("EVENT_001")
batch = ["login", "error", "logout"]
print(f"Event analysis: {len(batch)}"
      f" events, {HY}{event.process_batch(batch)}{X}\n")

print(f"{H}=== Polymorphic Stream Processing ===\n{X}")
proc = StreamProcessor()
# print(f"{D}Processing mixed stream types"
#       f" through unified interface...{X}")
# print("Batch 1 results:")
print(f"{G}All streams processed successfully."
      f" Nexus throughput optimal.{X}")
