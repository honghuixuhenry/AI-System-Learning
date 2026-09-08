from dataclasses import dataclass


@dataclass
class Endpoint:
    protocol: str
    host: str
    port: int
    path: str


    def url(self) -> str:

        return (
            f"{self.protocol}://"
            f"{self.host}:"
            f"{self.port}"
            f"{self.path}"
        )