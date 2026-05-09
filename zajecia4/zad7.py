def type_check(func):
    def wrapper(*args, **kwargs):
        for i in args:
            if not isinstance(i, int):
                raise TypeError(f"Expected int, got {type(i).__name__}")
        return func(*args, **kwargs)
    return wrapper

@type_check
def sum_all(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

def main():
    print(sum_all(1,2,3))
    print(sum_all(1, "a", 3))

if __name__ == "__main__":
    main()