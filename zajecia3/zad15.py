def get_pairs(l_lst, r_lst):
    i = 0
    while i < len(l_lst) and i < len(r_lst):
        yield tuple([l_lst[i], r_lst[i]])
        i += 1

def main():
    list1 = ["a", "aa", "aaa", "aaaa"]
    list2 = ["bbb", "bb", "b"]
    pairs = get_pairs(list1, list2)

    for i in pairs:
        print(i)

if __name__ == "__main__":
    main()
