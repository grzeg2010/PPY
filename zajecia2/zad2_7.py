def main():
    text = "123abc45"
    digits_count = 0
    for i in text:
        if '1' <= i <= '9':
            digits_count += 1
            # print(i)

    print(digits_count)

if __name__ == "__main__":
    main()
