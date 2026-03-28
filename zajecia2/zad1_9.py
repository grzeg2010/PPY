def main():
    print("Podaj liczbę N:")
    N = int(input())

    nums = []

    for i in range(0, N):
        print(f"Podaj {i+1}. liczbę: ")
        nums.append(
            int(input())
        )

    print(nums)

    nums_set = set()

    for number in nums:
        nums_set.add(number)

    print(nums_set)

if __name__ == "__main__":
    main()