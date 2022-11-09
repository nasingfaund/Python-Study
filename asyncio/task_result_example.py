import asyncio


async def long_operation(time):
    await asyncio.sleep(time)
    print(f'end of long_operation with {time} seconds')
    return 'some value'


async def some_action():
    print('start some_action...')
    print('end of some_action')


async def main():
    results = await asyncio.gather(
        long_operation(2),
        long_operation(4),
        long_operation(1),
        some_action()
    )
    print(results)


asyncio.run(main())
