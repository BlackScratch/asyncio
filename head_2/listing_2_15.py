from asyncio import Future
import asyncio
def make_request() -> Future:
    """Создать задачу, которая
асинхронно установит
значение future"""
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future

async def set_future_value(future) -> None:
    """Ждать 1 с, прежде чем
установить значение"""
    await asyncio.sleep(1)
    future.set_result(42)

async def main():
    """Приостановить main,
пока значение future
не установлено"""
    future = make_request()
    print(f'Будущий объект готов? {future.done()}')
    value = await future
    print(f'Будущий объект готов? {future.done()}')
    print(value)

asyncio.run(main())

"""Здесь мы определяем функцию make_request. 
В этой функции создается объект future и создается задача, которая 
асинхронно установит результат future через 1 с. Затем в функции main 
мы вызываем
make_request. Она сразу же возвращает неготовый будущий объект, не
содержащий результата, после чего мы применяем к нему await. 
Ожидание готовности этого объекта приостанавливает main на 1 с. Когда
ожидание завершится, value будет равно 42 и объект future станет готовым."""