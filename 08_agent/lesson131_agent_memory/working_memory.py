class WorkingMemory:

    def __init__(self):
        self.state = {}


    def set(
        self,
        key,
        value
    ):
        self.state[key] = value


    def get(
        self,
        key,
        default=None
    ):
        return self.state.get(
            key,
            default
        )


    def update(
        self,
        values
    ):
        self.state.update(
            values
        )


    def snapshot(self):
        return dict(
            self.state
        )


    def clear(self):
        self.state.clear()