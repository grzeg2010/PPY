# XVIII. Napisz program który powinien:
# 1. Pobierać liczbę od użytkownika.
# 2. Wypisać:
# • czy jest dodatnia/ujemna/zero
# • czy jest parzysta
# • jej zapis binarny i hex
# • jej kwadrat

user_input = int(input())

print("Number is: ")
if user_input > 0 :
    print("positive")
elif user_input < 0 :
    print("negative")
else :
    print("zero")

if user_input % 2 == 0 :
    print("even")
else :
    print("uneven")

print("in binary form: " + bin(user_input))
print("in hexadecimal form: " + hex(user_input))

print(str(user_input) + "*" + str(user_input) + "=" + str(pow(user_input, 2)))