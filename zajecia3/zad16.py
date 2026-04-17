def find_divisors(n):
    i = 1
    while i <= n:
        if n % i == 0:
            yield i
        i += 1

def main():
    divisors = find_divisors(105)

    for i in divisors:
        print(i)

if __name__ == "__main__":
    main()