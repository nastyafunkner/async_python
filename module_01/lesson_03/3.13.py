# Создайте три корутины, которые будут выводить следующие сообщения:
#
# Coroutine 1 is done
# Coroutine 2 is done
# Coroutine 3 is done
# Используя библиотеку asyncio, создайте три задачи для ранее созданных корутин.
#
# Запустите все задачи одновременно, используя asyncio.run().

import asyncio


async def coro_1():
    print('Coroutine 1 is done')


async def coro_2():
    print('Coroutine 2 is done')


async def coro_3():
    print('Coroutine 3 is done')


async def main():
    tasks = [
        asyncio.create_task(coro_1()),
        asyncio.create_task(coro_2()),
        asyncio.create_task(coro_3()),
    ]
    await asyncio.gather(*tasks)


asyncio.run(main())
