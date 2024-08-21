# Создайте асинхронную функцию (корутину) с именем main(), которая при вызове выводит на экран сообщение:
# Hello, Asyncio!
# Используйте функцию asyncio.run(), чтобы запустить вашу корутину.
# Убедитесь, что используемая вами версия Python 3.10 или выше.

import asyncio


async def main():
    print('Hello, Asyncio!')


asyncio.run(main())
