import random


def throw_dice():
    while True:
        throw = random.randint(1,6)
        yield throw
        if throw == 6:
            break

def main():
    throws = throw_dice()

    for i in throws:
        print(i)

if __name__ == "__main__":
    main()