# Napisz program analizujący wyniki studentów. Program powinien:
# • wygenerować dane dotyczące wyników studentów (liczba punktów z egzaminu),
# • przypisać studentom oceny na podstawie uzyskanej liczby punktów,
# • obliczyć średni wynik,
# • policzyć ilu studentów uzyskało ocenę pozytywną,
# • znaleźć trzy najlepsze wyniki.
# Na końcu program powinien wyświetlić podsumowanie wyników.

import random

students = [1,2,3,4,5,6,7,8]

score = dict()

scoreSum = 0

for student in students:
    score[student] = random.randint(0,100)

for student in students:
    scoreSum += score[student]
    if score[student] < 30:
        grade = 1
    elif score[student] < 50:
        grade = 2
    elif score[student] < 60:
        grade = 3
    elif score[student] < 70:
        grade = 4
    elif score[student] < 80:
        grade = 5
    else:
        grade = 6

    print(str(student) + ": " + str(score[student]))
    print("Grade: " + str(grade))

print("\nNumber of students: " + str(len(students)))
print("Score sum: " + str(scoreSum))
print("Average score: " + str(scoreSum / len(students)))
passing = sum(1 for s in students if score[s] >= 50)
print("Students with passing grade: " + str(passing))

scoreRanking = list(score.values())
scoreRanking.sort()
print("\n3 best scores: ")
for i in range (-3, 0):
    print(scoreRanking[i])