import asyncio


async def long_operation(time):
    await asyncio.sleep(time)
    print(f'end of long_operation with {time} seconds')
    return time


async def some_action():
    print('end of some_action')


# методы вызваны асинхронно => принты выведутся в порядке возрастания времени работы методов
async def main():
    task1 = asyncio.create_task(long_operation(2))
    task2 = asyncio.create_task(long_operation(4))
    task3 = asyncio.create_task(long_operation(1))
    task4 = asyncio.create_task(some_action())
    tasks = [task1, task2, task3, task4]

    # просто вызов
    # await asyncio.wait(tasks)

    # вызов с получением результатов
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
