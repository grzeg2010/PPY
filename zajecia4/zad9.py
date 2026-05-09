def auth_required(func):
    def wrapper(*args, **kwargs):
        if kwargs.get("user") == "admin":
            return func(*args, **kwargs)
        else:
            return None
    return wrapper

@auth_required
def add_numbers(a,b,user):
    return a + b

def main():
    print(add_numbers(1, 2, user="admin"))
    print(add_numbers(1, 2, user="adminos"))

if __name__ == "__main__":
    main()
