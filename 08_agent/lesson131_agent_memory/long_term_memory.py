class LongTermMemory:

    def __init__(self):
        self.store = {}


    def save(
        self,
        key,
        value
    ):
        self.store[key] = value


    def load(
        self,
        key,
        default=None
    ):
        return self.store.get(
            key,
            default
        )


    def delete(
        self,
        key
    ):
        self.store.pop(
            key,
            None
        )


    def all(self):
        return dict(
            self.store
        )