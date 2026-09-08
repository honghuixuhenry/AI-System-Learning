from memory_store import (
    MemoryItem,
    MemoryStore
)


class SecureMemory:

    def __init__(
        self,
        store: MemoryStore
    ):
        self.store = store


    def write(
        self,
        item: MemoryItem
    ) -> bool:

        if item.source in {
            "retrieved_document",
            "tool_output"
        }:
            return False

        if not item.verified:
            return False

        self.store.write(
            item
        )

        return True