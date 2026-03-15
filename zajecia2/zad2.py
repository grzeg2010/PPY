# Napisz program symulujący grę w zgadywanie liczby.
# Program powinien:
# • wybrać pewną liczbę z ustalonego zakresu,
# • umożliwić użytkownikowi zgadywanie tej liczby,
# • informować użytkownika, czy podana liczba jest większa czy mniejsza od szuka-
# nej,
# • zakończyć działanie po odgadnięciu liczby.
# Po zakończeniu gry program powinien:
# • wyświetlić liczbę prób,
# • wyświetlić wszystkie liczby podane przez użytkownika,
# • pokazać ostatnie próby zgadywania.
import random

random_number = random.randint(0,100)
print(random_number)

user_number = int(input())
user_numbers = {user_number}
last_tries = [user_number]
tries = 1

while random_number != user_number:
    if random_number < user_number:
        print("Your number is too big")
    else:
        print("Your number is too small")
    user_number = int(input())
    tries += 1
    user_numbers.add(user_number)
    last_tries.append(user_number)
    if len(last_tries) > 5:
        last_tries.pop(0)


print("You chose the correct number!")
print("Tries:" + str(tries))

print("Your numbers: ")
for number in user_numbers:
    print(number)

print("5 last tries:")
for number in last_tries:
    print(number)