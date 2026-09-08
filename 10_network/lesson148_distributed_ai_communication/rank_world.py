from dataclasses import dataclass


@dataclass
class Worker:
    rank: int
    world_size: int
    device: str


workers = [
    Worker(
        rank=i,
        world_size=4,
        device=f"gpu:{i}"
    )
    for i in range(4)
]


for worker in workers:
    print(worker)