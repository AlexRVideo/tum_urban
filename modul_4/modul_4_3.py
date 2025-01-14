def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

test_function()

try:
    inner_function()
except NameError:
    print("Произошла ошибка при попытке вызова внутренней функции inner_function вне функции test_function")