from typing import Any, List, Dict, Union, Optional # noqa
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return "Output: " + result


class NumericProcessor(DataProcessor):
    def __init__(self):
        print("Initializing Numeric Processor...")

    def process(self, data: Any) -> str:
        print("Processing data:", data)
        if self.validate(data):
            amount = len(data)
            total = sum(data)
            return f"{amount} {total} {total / len(data)}"
        return "Error!"

    def validate(self, data: Any) -> bool:
        print("Validation: ", end="")
        if not isinstance(data, List):
            print("Numeric data verification failed")
            return False
        for element in data:
            if not isinstance(element, (int, float)):
                print("Numeric data verification failed")
                return False
        print("Numeric data verified")
        return True

    def format_output(self, result: str) -> str:
        args = result.split()
        return f"Output: Processed {args[0]} numeric values: " \
               f"sum={args[1]}, avg={args[2]}"


class TextProcessor(DataProcessor):
    def __init__(self):
        print("Initializing Text Processor...")

    def process(self, data: Any) -> str:
        print("Processing data:", data)
        if self.validate(data):
            characters = len(data)
            words = len(data.split())
            return f"{characters} {words}"
        return "Error!"

    def validate(self, data: Any) -> bool:
        print("Validation: ", end="")
        if not isinstance(data, str):
            print("Text data verification failed")
            return False
        print("Text data verified")
        return True

    def format_output(self, result: str) -> str:
        args = result.split()
        return f"Output: Processed text: " \
               f"{args[0]} characters, {args[1]} words"


class LogProcessor(DataProcessor):
    def __init__(self):
        print("Initializing Log Processor...")

    def process(self, data: Any) -> str:
        print(f"Processing data: \"{data}\"")
        if self.validate(data):
            return data
        return "Error!"

    def validate(self, data: Any) -> bool:
        print("Validation: ", end="")
        if not isinstance(data, str):
            print("Log entry verification failed")
            return False
        if len(data.split()) < 2:
            print("Log entry verification failed")
            return False
        print("Log entry verified")
        return True

    def format_output(self, result: str) -> str:
        strs = result.split()
        level = strs[0].removesuffix(":").upper()
        del strs[0]
        result = " ".join(strs)
        return f"Output: [{level}] {level} level detected: {result}"


if __name__ == "__main__":
    def test_processor(proc: DataProcessor, data: Any) -> None:
        out = proc.process(data)
        print(proc.format_output(out))

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    test_processor(NumericProcessor(), [1, 2, 3, 4, 5])
    test_processor(TextProcessor(), "Hello Nexus World")
    test_processor(LogProcessor(), "ERROR: Connection timeout")
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    test_processor(NumericProcessor(), [1, 2, 3])
    test_processor(TextProcessor(), "Hey guys")
    test_processor(LogProcessor(), "INFO: System ready")
    print("Foundation systems online. Nexus ready for advanced streams.")
