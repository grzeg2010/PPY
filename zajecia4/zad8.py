def safe_execution(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {type(e).__name__}: {e}")
    return wrapper

@safe_execution
def divide(a, b):
    return a / b

def main():
    print(divide(10, 2))   # 5.0
    print(divide(10, 0))   # prints error, does not crash
    print(divide(10, 2))   # 5.0

if __name__ == "__main__":
    main()