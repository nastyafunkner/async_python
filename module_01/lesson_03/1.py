import asyncio


async def slow_operation():
    print("Slow operation result")


async def main():
    slow_operation()


asyncio.run(main())
