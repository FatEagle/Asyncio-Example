import asyncio
import random


async def random_value(flag=True):
    value = random.randint(0, 100)
    if not flag:
        value += 0.555

    return value


async def print_value(value):
    another = await random_value(False)

    print(f"new value: {value}")
    print(f"another value: {another}")


async def executor():
    while True:
        # do something
        await asyncio.sleep(2)
        result = await random_value()
        await print_value(result)


if __name__ == '__main__':
    # execute in Python3.7+
    asyncio.run(executor())

    # execute in Python3.6+
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(print_result())
    # loop.close()
