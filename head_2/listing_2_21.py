import asyncio
async def main():
    await asyncio.sleep(1)
loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()

"""Это похоже на то, что происходит при вызове asyncio.run, с той
разницей, что оставшиеся задачи не отменяются. Если нам нужна
специальная логика очистки, то ее следует реализовать в предложении finally"""