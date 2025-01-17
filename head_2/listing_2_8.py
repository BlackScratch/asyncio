"""Для создания задачи служит функция asyncio.create_task. Ей передается подлежащая выполнению сопрограмма, а в ответ она немедленно возвращает объект задачи. Этот объект можно включить в выражение await, которое извлечет возвращенное значение по завершении
задачи."""

import asyncio
from utils.delay_functions import delay
async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    result = await sleep_for_three
    print(result)
asyncio.run(main())

"""Здесь мы создали задачу, которой для выполнения нужно 3 с. Кроме того, мы печатаем тип задачи, в данном случае <class '_asyncio.
Task'>, чтобы показать, что это не сопрограмма.

Следует также отметить, что предложение печати выполняется
сразу после запуска задачи. Если бы мы просто использовали await
для сопрограммы delay, то увидели бы сообщение только через 3 с.
Напечатав сообщение, мы применяем await к задаче sleep_for_
three. Это приостанавливает сопрограмму main до получения результата от задачи."""

