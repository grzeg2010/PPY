def repeat(n):
    def repeat_deco(func):
        def wrapper(*args, **kwargs):
            for i in range (n - 1):
                func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return repeat_deco

@repeat(3)
def greet ( name ) :
    print ( f" Hello { name }" )

greet("greg")