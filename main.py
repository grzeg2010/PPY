# mutable, non mutable

n = 5
print(id(n)) #140732142666792
n = 10
print(id(n)) #140732142666952
# a więc immutable

n = 63920627967848603809243702730707904279607626374378375483560923526392062796784860380924370273070790427960762637437837
print(type(n))

n = "Hey man"
print(type(n))

if n or 2:
    print(n)

for i in range(3, 10):
    print(i)

for i in range(3, 10, 2): # co druga liczba
    print(i)

for i in "abcde":
    print(i)

# non iterable
# for i in 5:
#     print(i)
#     print(i)

n = "Ala ma kota"
print(n[0])
print(n[0:4])
print(n[0:6:2])

print("Ala", "ma", "kota", sep="^", end=".")
print("A kot ma Ale")

a, b, c = 1, 2, 3
print(a, b, c)

a = 10
b = 20
a,b = b,a
print(a,b)