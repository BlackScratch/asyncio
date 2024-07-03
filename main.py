import asyncio

import asyncio
async def main():
    print('Hello...')
    await asyncio.sleep(1)
    print('World!')


async def my_coroutine():
    print("Запуск корутины")
    await asyncio.sleep(1) # Приостановка корутины на 1 секунду
    print("Завершение корутины")
# Создание задачи из корутины
async def main():
    task = asyncio.create_task(my_coroutine())
    await task
# Запуск event loop

# Определение асинхронной функции (корутины) cook_dish(n), которая имитирует повара, готовящего блюдо.
# Используется корутина для того, чтобы одновременно запускать несколько "поваров" и использовать время ожидания (приготовление) эффективно.
async def cook_dish(n):
    print(f"Повар {n} начинает готовить") # Повар n начинает готовить
    await asyncio.sleep(n) # Повар готовит блюдо n секунд.asyncio.sleep(n) используется для имитации задержки, которая требуется дляприготовления блюда.
    print(f"Повар {n} закончил готовить") # Повар n закончил готовить
    return f"Блюдо от повара {n}" # Возвращает строку, указывающую, что блюдо от повара n готово.
    # Создание задач из корутин, которые представляют собой приготовление блюда каждым поваром.
async def main():
    tasks = [asyncio.create_task(cook_dish(n)) for n in range(1, 4)] # Создаются задачи для каждого повара (от 1 до 3). Используется create_task для запуска корутины.
    print(await asyncio.gather(*tasks)) # Ожидает завершения всех задач, затем выводит результат. asyncio.gather используется для ожидания всех корутин, затем собирает их результаты в список.
    # Запуск главной корутины


asyncio.run(main())

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
