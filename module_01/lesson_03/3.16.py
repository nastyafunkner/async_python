import asyncio

# Counter 1 - имя счётчика
# 13 - максимальное значение для счётчика Counter_1
max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15,
}

# Создайте словарь counters, где ключи — это имена счётчиков ("Counter 1" и "Counter 2"),
# а значения — это текущие значения счётчиков, изначально равные нулю.
counters = {
    "Counter 1": 0,
    "Counter 2": 0,
    "Counter 3": 0,
}

delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5,
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
        await asyncio.sleep(counter_sleep)
        print(f'{counter_name}: {counters[counter_name]}')


async def do():
    tasks = [asyncio.create_task(counter(f"Counter {i}", delays[f"Counter {i}"])) for i in range(1, 4)]
    await asyncio.gather(*tasks)


asyncio.run(do())
