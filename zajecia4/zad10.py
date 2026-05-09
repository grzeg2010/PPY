def retry(n):
    def retry_decor(func):
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, n + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt}/{n} failed: {e}")
            raise last_exception
        return wrapper
    return retry_decor

@retry(3)
def unstable():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success"

def main():
    try:
        print(unstable())
    except Exception as e:
        print(f"All attempts exhausted: {e}")

if __name__ == "__main__":
    main()
