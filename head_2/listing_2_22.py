import asyncio
import asyncio
from utils.asyncio_timed import async_timed
from utils.delay_functions import delay
import requests
def call_later():
    print("Меня вызовут в ближайшем будущем!")
async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)
asyncio.run(main())