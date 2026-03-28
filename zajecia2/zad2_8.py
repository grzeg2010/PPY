def main():
    sum = 0
    text = "123abc45"
    for i in text:
        if '1' <= i <= '9':
            sum += int(i)

    print(sum)

if __name__ == "__main__":
    main()