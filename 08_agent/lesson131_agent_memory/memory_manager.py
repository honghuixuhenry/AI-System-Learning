from conversation_memory import (
    ConversationMemory
)

from working_memory import (
    WorkingMemory
)

from long_term_memory import (
    LongTermMemory
)


class MemoryManager:

    def __init__(self):

        self.conversation = (
            ConversationMemory()
        )

        self.working = (
            WorkingMemory()
        )

        self.long_term = (
            LongTermMemory()
        )