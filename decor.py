def decorator_function(func):
    res = func()
    return res.upper()


@decorator_function
def hello_world():
    return 'hello world!'


print(hello_world)
