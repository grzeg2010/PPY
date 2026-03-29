def fib(n=15):
    a,b = 0,1
    while b < n:
        yield b
        a, b = b, a+b

for i in fib(100):
    print(i)