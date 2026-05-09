from time import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        f = func(*args, **kwargs)
        print(time() - start)
        return f
    return wrapper

@timer
def slow_add(a,b):
    import time
    time.sleep(1)
    return a+b

print(slow_add(5,8))
