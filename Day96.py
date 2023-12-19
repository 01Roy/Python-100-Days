import asyncio


async def hello_world():
    print("Hello")


async def delayed_print():
    await asyncio.sleep(1)
    print("world")


async def main():
    task1 = asyncio.create_task(hello_world())
    task2 = asyncio.create_task(delayed_print())

    await task1
    await task2


asyncio.run(main())
