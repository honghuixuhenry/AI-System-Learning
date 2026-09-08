class Memory:

    def __init__(self):
        self._data = {}


    def write(
        self,
        key,
        value
    ):
        self._data[key] = value


    def read(
        self,
        key,
        default=None
    ):
        return self._data.get(
            key,
            default
        )


    def snapshot(self):
        return dict(
            self._data
        )