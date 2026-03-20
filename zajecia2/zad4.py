# Napisz program symulujący koszyk zakupowy.
# Program powinien:
# • umożliwić użytkownikowi dodawanie produktów wraz z ich cenami,
# • zakończyć wprowadzanie danych po spełnieniu określonego warunku,
# • obliczyć całkowitą wartość zakupów,
# • znaleźć najdroższy produkt,
# • obliczyć średnią cenę produktu.
# Na końcu program powinien wyświetlić podsumowanie koszyka.

products = dict[str, float]()

add_more_products = True

while add_more_products:
    print("Dodaj produkt: ")
    user_key = str(input())
    if user_key != "ok":
        print("Podaj cenę: ")
        user_price = float(input())
        products[user_key] = user_price
    else:
        add_more_products = False

total_sum = 0

for item in products:
    total_sum = sum(products.values())

most_expensive = max(products, key=products.get)

average_price = total_sum / len(products)

print("Cena: " + str(total_sum))
print("Najdrozszy produkt: " + most_expensive + ". Cena: " + str(products[most_expensive]))
print("Średnia cena: " + str(average_price))