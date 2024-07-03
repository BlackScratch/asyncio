import asyncio

async def hello_worls_message() -> str:
    await asyncio.sleep(1)
    return "Hello World"

async def main()-> None:
    message = await hello_worls_message()
    print(message)
asyncio.run(main())