class SimpleEnvironment:

    def __init__(self):
        self.weather = {
            "Atlanta": 86,
            "New York": 75
        }

    def get_weather(
        self,
        city
    ):
        return self.weather.get(
            city
        )