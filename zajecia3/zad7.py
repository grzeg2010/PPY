def generator(lst):
    for i in range(0, len(lst), 2):
        yield tuple(lst[i:i+2])

gen = generator([6,5,2,4,8])
for i in gen:
    print(i)