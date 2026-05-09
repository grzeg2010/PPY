import time
import functools

def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@memoize
def slow_add(a,b):
    """ Simulates a slow addition by sleeping for 1 second ."""
    time.sleep(1)
    print(f" Computing {a} + {b}... ")
    return a + b

def main():
    print(slow_add(2, 3))  # powinno w y p i s a " Computing 2 + 3 . . . " i zwroci 5
    print(slow_add(2, 3))  # powinno n a t y c h m i a s t z w r c i 5 bez wypisywania
    print(slow_add(3, 4))  # powinno w y p i s a " Computing 3 + 4 . . . " i zwrci 7

if __name__ == "__main__":
    main()