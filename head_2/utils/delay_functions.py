import asyncio

async def delay(delay_seconds: int) -> int:
    print(f"Засыпааю на {delay_seconds} с")
    await  asyncio.sleep(delay_seconds)
    print(f"Сон на {delay_seconds} с закончился")
    return delay_seconds
