def uppercase(func):
    def wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        return f.upper()
    return wrapper

if __name__ == "__main__":
    @uppercase
    def concat_strings(text, more_text):
        return text + more_text

    print(concat_strings("test", "hello"))