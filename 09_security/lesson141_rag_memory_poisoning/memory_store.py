from dataclasses import dataclass
from typing import List


@dataclass
class MemoryItem:
    key: str
    value: str
    source: str
    verified: bool


class MemoryStore:

    def __init__(self):
        self.items: List[MemoryItem] = []


    def write(
        self,
        item: MemoryItem
    ):
        self.items.append(item)


    def read_all(self):
        return list(self.items)