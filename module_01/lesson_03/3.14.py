# Создайте корутину print_with_delay(), которая принимает целое число в качестве аргумента
# и выводит сообщение следующего типа:
# f'Coroutine {num} is done'
# Используя только что созданную корутину, создайте 10 задач (tasks) для асинхронного выполнения.
# При создании каждой задачи передавайте в print_with_delay() числа от 0 до 9.
# Задачи должны быть запущены асинхронно и выполнены примерно в секундном интервале времени.
# Сообщения должны быть выведены задачами в строгом порядке от 0 до 9 в соответствии с Sample Output.
# P.S. После того как решите задачу, обязательно ознакомьтесь с решениями других студентов.
# Возможно, вы найдете несколько интересных подходов!

import asyncio


async def print_with_delay(num: int):
    print(f'Coroutine {num} is done')
    await asyncio.sleep(1)


async def do():
    tasks = [asyncio.create_task(print_with_delay(i)) for i in range(10)]
    await asyncio.gather(*tasks)


asyncio.run(do())
