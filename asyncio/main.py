import time
import asyncio

"""
https://habr.com/ru/post/667630/

корутина - сущность, возвращаемая асинхронным методом (методом с модификатором async)
корутина схожа с генератором
event-loop (цикл событий) - цикл, прокручивающий корутины
футуры - объекты, хранящие результаты выполнения корутин
"""

"""
синхронный метод с блокирующим sleep
"""
def send_request():
    print('  make a request...')
    time.sleep(1.5)


"""
асинхронный метод с неблокирующим sleep
"""
async def async_send_request():
    print('  make a request...')
    await asyncio.sleep(1.5)


# ASYNC CODE
async def async_func(count):
    tasks = [asyncio.create_task(async_send_request()) for _ in range(count)]
    await asyncio.wait(tasks)


COUNT = 5

# sync code
# print(f"start: {time.strftime('%X')}")
# [send_request() for _ in range(COUNT)]
# print(f"end: {time.strftime('%X')}", end='\n\n')

# async code
print(f"start: {time.strftime('%X')}")
asyncio.run(async_func(COUNT))
print(f"end: {time.strftime('%X')}")
