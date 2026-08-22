def add(a: int, b: int) -> int:
    return a+b

def divide(a: float, b: float) -> float:
    return a/b

from typing import List, Dict, Optional
def average(nums: List[int]) -> float:
    return sum(nums) / len(nums)


def load(config: Dict[str, str]):
    ...

def load(model: Optional[str]):
    ...

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int

s = Student("Alice", 20)
print(s)

from enum import Enum

class ModelType(Enum):
    QWEN = "Qwen"
    LLAMA = "Llama"
    DEEPSEEK = "DeepSeek"

@dataclass
class Config: 
    model: ModelType
    max_tokens: int
    temperature: float

config = Config(model=ModelType.QWEN, max_tokens=2048, temperature=0.7)