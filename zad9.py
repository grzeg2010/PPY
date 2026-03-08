import sys

power = 2 ** 200

print(power)
print(type(power))
print(power.__sizeof__())

smallInt = 3
print(smallInt.__sizeof__())
biggerInt = 4096
print(biggerInt.__sizeof__())

print(sys.maxsize)