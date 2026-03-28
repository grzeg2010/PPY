def main():
    for i in range(1,51):
        if i % 3 == 0:
            print(f"{i} - divisible by 3") # TODO 15, 30 are divisible by both
        elif i % 5 == 0:
            print(f"{i} - divisible by 5")
        else:
            print(i)

if __name__ == "__main__":
    main()