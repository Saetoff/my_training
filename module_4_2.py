def test_function():
    def inner_function():
        print(f'область видимости')
    inner_function()


#inner_function() # вызов функций вне test_function
test_function()