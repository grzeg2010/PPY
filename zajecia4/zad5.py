def call_counter(func):
    i = 0

    def wrapper(*args, **kwargs):
        nonlocal i
        f = func(*args, **kwargs)
        i += 1
        print(i)
        return f
    return wrapper

@call_counter
def random_cout():
    print("hehe")

@call_counter
def random_bool():
    print(False)

def main():
    random_cout()
    random_cout()
    random_cout()
    random_bool()
    random_bool()
    random_cout()

if __name__ == "__main__":
    main()
