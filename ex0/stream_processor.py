#!/usr/bin/env python3

from typing import Any, List
from abc import ABC, abstractmethod

X = "\033[0m"
R = "\033[91m"
G = "\033[92m"
H = "\033[1m"
D = "\033[2m"


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
        print(f"{D}\nInitializing Numeric Processor...{X}")

    def process(self, data: Any) -> str:
        print("Processing data:", data)
        if self.validate(data):
            amount = len(data)
            total = sum(data)
            return f"{amount} {total} {total / len(data)}"
        raise TypeError(f"input '{data}' is invalid for NumericProcessor")

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
        return f"Processed {args[0]} numeric values: " \
               f"sum={args[1]}, avg={args[2]}"


class TextProcessor(DataProcessor):
    def __init__(self):
        print(f"{D}\nInitializing Text Processor...{X}")

    def process(self, data: Any) -> str:
        print("Processing data:", data)
        if self.validate(data):
            characters = len(data)
            words = len(data.split())
            return f"{characters} {words}"
        raise TypeError(f"input '{data}' is invalid for TextProcessor")

    def validate(self, data: Any) -> bool:
        print("Validation: ", end="")
        if not isinstance(data, str):
            print("Text data verification failed")
            return False
        print("Text data verified")
        return True

    def format_output(self, result: str) -> str:
        args = result.split()
        return f"Processed text: " \
               f"{args[0]} characters, {args[1]} words"


class LogProcessor(DataProcessor):
    def __init__(self):
        print(f"{D}\nInitializing Log Processor...{X}")

    def process(self, data: Any) -> str:
        print(f"Processing data: \"{data}\"")
        if self.validate(data):
            return data
        raise TypeError(f"input '{data}' is invalid for LogProcessor")

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
        return f"[{level}] {level} level detected: {result}"


if __name__ == "__main__":
    def test_processor(proc: DataProcessor, data: Any) -> None:
        try:
            out = proc.process(data)
            print(f"Output: {proc.format_output(out)}")
        except TypeError as e:
            print(f"{R}Error: {e}{X}")

    print(f"{H}\n=== CODE NEXUS - DATA PROCESSOR FOUNDATION ==={X}")
    num = NumericProcessor()
    test_processor(num, [1, 2, 3, 4, 5])
    txt = TextProcessor()
    test_processor(txt, "Hello Nexus World")
    log = LogProcessor()
    test_processor(log, "ERROR: Connection timeout")
    print(f"{H}\n=== Polymorphic Processing Demo ==={X}")
    print(f"{D}Processing multiple data types through same interface...{X}")
    test_processor(num, [1, 2, 3])
    print()
    test_processor(txt, "Hey guys")
    print()
    test_processor(log, "INFO: System ready")
    print(f"{G}\nFoundation systems online."
          f" Nexus ready for advanced streams.{X}")
