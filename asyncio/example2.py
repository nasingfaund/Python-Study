import asyncio
import time
import requests
from aiohttp import ClientSession

URL = f'http://api.openweathermap.org/data/2.5/weather'
TOKEN = '2a4ff86f9aaa70041ec8e82db64abf56'

PARAMS = {
    'q': None,
    'APPID': TOKEN
}

cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']


# синхронный вариант
def print_weather(cities_, url, params):

    for city in cities_:
        params['q'] = city
        response = requests.get(url=url, params=params).json()
        print(f'{city}: {response["weather"][0]["main"]}')


# асинхронный вариант
async def get_weather_async(city, url, params):
    async with ClientSession() as session:
        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            return f'{city}: {weather_json["weather"][0]["main"]}'


async def print_weather_async(cities_, url, params):
    tasks = []
    for city in cities_:
        params['q'] = city
        tasks.append(asyncio.create_task(get_weather_async(city, url, params)))

    # gather используется для получения возвращаемых значений тасков
    results = await asyncio.gather(*tasks)
    [print(result) for result in results]

    # вариант вызова для таска, не возвращающего значение, а печатающего информацию
    # await asyncio.wait(tasks)


print(time.strftime('%X'))

# SYNC
# print_weather(cities, URL, PARAMS)

# ASYNC
asyncio.run(print_weather_async(cities, URL, PARAMS))

print(time.strftime('%X'))
