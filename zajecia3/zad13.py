def words_lengths(lst):
    i = 0
    while i < len(lst):
        if len(lst[i]) > 3:
            yield len(lst[i])
        i += 1

def main():
    words = ["a", "ab", "abc", "kotek", "słuchawki"]
    lengths = words_lengths(words)

    for i in lengths:
        print(i)

if __name__ == "__main__":
    main()