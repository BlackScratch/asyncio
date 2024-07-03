import functools
import time
from typing import Callable, Any
def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'выполняется {func} с аргументами {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'{func} завершилась за {total:.4f} с')
        return wrapped
    return wrapper

"""Здесь мы создаем новую сопрограмму wrapped. Это обертка вокруг
исходной сопрограммы, которая принимает ее аргументы, *args
и **kwargs, выполняет предложение await и возвращает результат.
Мы окружили это предложение двумя сообщениями: одно печатается в начале выполнения функции, а второе в конце. В них отображаются время начала и завершения точно так же, как мы делали в пре64 Глава 2 Основы asyncio
дыдущих примерах. Теперь можно добавить к любой сопрограмме
этот декоратор в виде аннотации и увидеть, сколько времени она
работала."""