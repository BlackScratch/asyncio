import asyncio
from asyncio import CancelledError
from utils.delay_functions import delay
"""Проверять состояние каждую секунду или с другим интервалом, как
в предыдущем примере, – не самый простой способ реализации таймаута. В идеале хотелось бы иметь вспомогательную функцию, которая
позволяла бы задать тайм-аут и снять задачу по его истечении.
В asyncio есть такая возможность в виде функции asyncio.wait_for.
Она принимает объект сопрограммы или задачи и тайм-аут в секун58 Глава 2 Основы asyncio
дах и возвращает сопрограмму, к которой можно применить await.
Если задача не завершилась в отведенное время, то возбуждается исключение TimeoutError и задача автоматически снимается.
Для иллюстрации работы wait_for мы рассмотрим случай, когда задаче требуется две секунды, но мы даем ей только одну. Мы перехватываем исключение TimeoutError и смотрим, была ли задача снята."""
async def main():
    delay_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Тайм-аут!')
        print(f'Задача была снята? {delay_task.cancelled()}')
asyncio.run(main())