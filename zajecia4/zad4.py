from time import sleep, time


def delay(seconds):
    def delay_deco(func):
        def wrapper(*args, **kwargs):
            f = func(*args, **kwargs)
            sleep(seconds)
            return f
        return wrapper
    return delay_deco

def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        f = func(*args, **kwargs)
        print(time() - start)
        return f
    return wrapper

@timer
@delay(2)
def fetch_data():
    return "data"

def main():
    print(fetch_data())

if __name__ == "__main__":
    main()