import asyncio
from utils.delay_functions import delay

async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print("Пока я жду, то исполняется другой код")

async def main():
    """Сначала мы запускаем две задачи, которые спят в течение 3 с; пока
эти задачи простаивают, мы видим, как каждую секунду печатается
сообщение «пока я жду, исполняется другой код!». Это означает, что
даже во время выполнения длительных операций наше приложение
может выполнять другие задачи.
Потенциальная проблема заключается в том, что задача может работать неопределенно долго. Быть может, нам захочется остановить
задачу, если она никак не кончается сама. Такая возможность поддерживается и называется снятием."""
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))
    await hello_every_second()
    await first_delay
    await second_delay

asyncio.run(main())