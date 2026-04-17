def reverse_numbers(lst):
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]

def main():
    numbers = [15, 97, 14, 6, 53]
    reversed = reverse_numbers(numbers)

    for i in reversed:
        print(i)

if __name__ == "__main__":
    main()