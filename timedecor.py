import time


def time_dec(func):
    def wrapper(*args, **kwargs):
        t = time.time()
        result = func(*args, **kwargs)
        print("Время: ",  time.time() - t)
        return result
    return wrapper


@time_dec
def fib(n=100):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b


print(fib(101))
