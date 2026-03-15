# Napisz program analizujący dane liczbowe.
# Program powinien:
# • wygenerować zbiór losowych liczb,
# • usunąc ewentualne duplikaty,
# • znaleźć największą i najmniejszą wartość,
# • określić ile elementów spełnia określony warunek (np. jest większych od śred-
# niej).
# Dodatkowo program powinien:
# • wyświetlić wybrane elementy danych,
# • znaleźć drugą największą wartość.
import random

random_numbers = set()
for i in range(0,15):
    random_numbers.add(random.randint(0,10))

numbers_sum = 0

for number in random_numbers:
    print(number)
    numbers_sum += number

average = numbers_sum / len(random_numbers)
bigger_than_average = 0

sorted_numbers = sorted(random_numbers)
print("Smallest value: " + str(sorted_numbers[0]))
print("Biggest value: " + str(sorted_numbers[-1]))
print("Second biggest value: " + str(sorted_numbers[-2]))

print("Average: " + str(average))
for number in random_numbers:
    if number > average:
        bigger_than_average += 1
print("Number of numbers bigger than the average: " + str(bigger_than_average))