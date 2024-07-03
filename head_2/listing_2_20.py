"""Неправильное использование блокирующего API
как сопрограммы"""
import asyncio
from utils.asyncio_timed import async_timed
from utils.delay_functions import delay
import requests
@async_timed()
async def get_example_status() -> int:
    return requests.get('http://www.example.com').status_code
@async_timed()
async def main():
    task_1 = asyncio.create_task(get_example_status())
    task_2 = asyncio.create_task(get_example_status())
    task_3 = asyncio.create_task(get_example_status())
    await task_1
    await task_2
    await task_3
asyncio.run(main())

"""Результат выполнения этой программы показан ниже. Обратите
внимание, что полное время работы сопрограммы main 
приблизительно равно сумме времен запущенных задач получения кода состояния, 
т. е. мы не получили никакого выигрыша от конкурентностиИ снова причина 
в том, что библиотека requests блокирующая, т. е.
блокирует поток, в котором выполняется. Поскольку asyncio однопоточная, 
библиотека requests блокирует цикл событий и не дает ничему выполняться 
конкурентно."""