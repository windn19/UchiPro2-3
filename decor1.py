def decor_func(func):
    def swap():
        return func().upper()
    return swap


@decor_func
def hello_world():
    return 'Hello, World!!!'


print(hello_world())
