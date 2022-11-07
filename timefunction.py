from time import time
from functools import wraps


def time_function(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print(f.__name__ + " " + "took" + " " + str((end - start) * 1000) + 'ms')
        return result
    return wrapper


@time_function
def interesting_function():
    print('hello')


interesting_function()
