from asyncio import Future
my_future = Future()
print(f'my_future готов? {my_future.done()}')
my_future.set_result(42)
print(f'my_future готов? {my_future.done()}')
print(f'Какой результат хранится в my_future? {my_future.result()}')

"""Будущие объекты также можно использовать в выражениях await.
Это означает «я посплю, пока в будущем объекте не будет установлено 
значение, с которым я могу работать, 
а когда оно появится, разбуди меня и дай возможность его обработать»."""