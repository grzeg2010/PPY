def squares_of_2():
    i = 1
    while True:
        i += 1
        result = pow(2,i)
        if result < 1000:
            yield pow(2, i)
        else:
            break

sq = squares_of_2()
for i in sq:
    print(i)
