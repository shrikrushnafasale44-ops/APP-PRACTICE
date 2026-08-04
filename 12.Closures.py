def outer(message):
    def inner():
        print(message)
    return inner

my_function = outer("Hello, Python!")

my_function()
