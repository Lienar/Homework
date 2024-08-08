import time
import asyncio

async def start_strongman(name, power):

    print (f'Силач {name} начал соревнования.')
    start = time.time()
    for i in range (1, 6):
        if 1 == 1:
            print(f'Силач {name} поднял {i}' )
            await asyncio.sleep(15/power)
        else:
            await asyncio.sleep(1)
            print(f'Силач {name} поднял {i}')
            await asyncio.sleep(15 / power)
    finish = time.time()
    delta = finish - start
    print(f'Силач {name} закончил соревнования за {delta}.')


async def start_tournament():
    competitor1 = asyncio.create_task(start_strongman('Pasha', 3))
    competitor2 = asyncio.create_task(start_strongman('Denis', 4))
    competitor3 = asyncio.create_task(start_strongman('Apollon', 5))
    await competitor1
    await competitor2
    await competitor3


asyncio.run(start_tournament())