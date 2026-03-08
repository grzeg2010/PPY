print("Podaj", "pierwszą", "liczbę")
a = int(input())
print("Podaj drugą" + "liczbę")
b = int(input())

operacje = ["suma", "różnica", "iloczyn", "dzielenie", "dzielenie całkowite", "potęgowanie"]

result = a + b
print(operacje[0] + ": wynik to: " + str(result))

result = a - b
print(operacje[1] + ": wynik to: " + str(result))

result = a * b
print(operacje[2] + ": wynik to: " + str(result))

result = a / b
print(operacje[3] + ": wynik to: " + str(result))

result = a // b
print(operacje[4] + ": wynik to: " + str(result))

result = a ** b
print(operacje[5], "wynik to", str(result), sep=": ")

print("""
Dziękujemy za skorzystanie z naszej aplikacji
Firma kalkex
Pozdrowienia
""")