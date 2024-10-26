def test_function():
    def inner_function():
        print(f'область видимости')
    inner_function()


test_function()