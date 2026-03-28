import random

N = int(input())

lst = []

def is_divided_by_5(checked_number):
    return checked_number % 5 == 0

i = 0
number = 1

while i < N:
    if is_divided_by_5(number):
        lst.append(number)
        i += 1

    number += 1

for number in lst:
    print(number)

# TODO complete extra requirements