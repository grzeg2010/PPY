def gen():
    print("Hello")
    yield 1
    print("World")
    yield 2
    yield 3

print(gen())
gen_expr = (i for i in range(5))
print(gen_expr)

g = gen()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))

gen_expr = (i for i in range(5))
print(gen_expr)
print(next(gen_expr))
print(next(gen_expr))
print(next(gen_expr))
print(next(gen_expr))
print(next(gen_expr))
# print(next(gen_expr))

gen_expr = (i for i in range(5))
print(gen_expr)
for i in gen_expr:
    print(i)

print(gen())
g = gen()
for i in g:
    print(i)
g2 = gen()
for i in g2:
    print(i)

# ---------------------------------------
# ---------------------------------------
# ---------------------------------------
from random import randint

def roll_dice(n=6): # rzuty zakończą się, gdy zostanie wylosowane n
    while True:
        num = randint(1,6)
        yield num
        if num == n:
            break

roll = roll_dice()
print(roll)
for i in roll:
    print(i)

from time import sleep

def fib():
    a,b=0,1
    while True:
        yield b
        a, b = b, a+b

for i in fib():
    print(i)
    sleep(0.2)
