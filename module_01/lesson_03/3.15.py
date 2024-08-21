import asyncio

# Counter 1 - имя счётчика
# 13 - максимальное значение для счётчика Counter_1
max_counts = {
    "Counter 1": 13,
    "Counter 2": 7,
}

# Создайте словарь counters, где ключи — это имена счётчиков ("Counter 1" и "Counter 2"),
# а значения — это текущие значения счётчиков, изначально равные нулю.
counters = {
    "Counter 1": 0,
    "Counter 2": 0,
}


# Используйте словарь max_counts, где ключи представляют собой имена счётчиков,
# а значения — это максимальное число, до которого каждый счётчик должен подсчитать.
# Напишите асинхронную функцию counter, которая принимает имя счётчика и задержку.
# В цикле эта функция должна увеличивать значение соответствующего счётчика в словаре counters на 1,
# затем делать паузу на заданное количество секунд,
# затем выводить сообщение с именем счетчика и его текущим значением.
# Этот цикл должен продолжаться до тех пор,
# пока значение счётчика не достигнет соответствующего значения в словаре max_counts.
async def counter(counter_name, counter_sleep):
    while counters[counter_name] < max_counts[counter_name]:
        counters[counter_name] += 1
        print(f'{counter_name}: {counters[counter_name]}')
        await asyncio.sleep(counter_sleep)


# В асинхронной функции main создайте две задачи с использованием asyncio.create_task(),
# каждая из которых будет выполнять функцию counter с разными именами счётчиков,
# но с одинаковой фиксированной задержкой.
# Эта функция должна ожидать завершения обеих задач.
async def do():
    tasks = [
        asyncio.create_task(counter("Counter 1", 1)),
        asyncio.create_task(counter("Counter 2", 1)),
    ]
    await asyncio.gather(*tasks)


asyncio.run(do())
