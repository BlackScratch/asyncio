import asyncio
from asyncio import CancelledError
from utils.delay_functions import delay
async def main():
    """
    Note:
    Здесь мы создаем задачу, работающую 10 с. Затем в цикле while
проверяем состояние задачи. Метод задачи done возвращает True,
если задача завершилась, и False в противном случае. Каждую секунду мы проверяем, завершилась ли задача, и запоминаем, сколько
секунд уже прошло. Если задача работает дольше 5 с, то мы ее снимаем. Далее задача запускается в предложении await long_task и, если
возникло исключение CancelledError, печатается сообщение «Наша
задача была снята».


seconds_elapsed:int
    Полный путь до текстового файла

Важно отметить, что исключение CancelledError может быть возбуждено только внутри предложения await. То есть, если вызвать метод cancel, когда задача исполняет Python-код, этот код будет продолжать работать, пока не встретится следующее предложение await
(если встретится), и только тогда будет возбуждено исключение CancelledError. Вызов cancel не прерывает задачу, делающую свое дело;
он снимает ее, только если она уже находится в точке ожидания или
когда дойдет до следующей такой точки."""
    long_task = asyncio.create_task(delay(10))
    seconds_elapsed = 0
    while not long_task.done():
        print('Задача не закончилась, следующая проверка через секунду.')
        await asyncio.sleep(1)
        seconds_elapsed = seconds_elapsed + 1
        if seconds_elapsed == 5:
            long_task.cancel()
    try:
        await long_task
    except CancelledError:
        print('Наша задача была снята')
asyncio.run(main())