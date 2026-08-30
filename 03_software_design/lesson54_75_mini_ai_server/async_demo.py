import asyncio

# async def hello():
#     print("Hello")

# asyncio.run(hello())

# import asyncio

# async def task():
#     print("Start")
#     await asyncio.sleep(2)
#     print("End")

# asyncio.run(task())

# async def task_a():
#     print("A Start")
#     await asyncio.sleep(3)
#     print("A End")

# async def task_b():
#     print("B Start")
#     await asyncio.sleep(2)
#     print("B End")

# async def main():
#     await asyncio.gather(
#         task_a(),
#         task_b()
#     )

# asyncio.run(main())

async def download(name, seconds):
    print(f"{name} started")
    await asyncio.sleep(seconds)
    print(f"{name} finished")
    return name

async def main():
    results = await asyncio.gather(
        download("File A", 3),
        download("File B", 2),
        download("File C", 1)
    )
    print(results)

asyncio.run(main())