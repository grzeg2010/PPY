# Pobierz zdanie.
# Sprawdź:
# • czy zawiera słowo "Python"
# • ile razy występuje litera "a"
# • Zamień "Python"na "JAVA".

user_input = str(input())

contains_python = user_input.find("Python")
if user_input.find("Python") == -1 :
    contains_python = False
else :
    contains_python = True

print("Contain word \"Python\": " + str(contains_python))

a_count = user_input.count("a")
print("Number of letters \"a\": " + str(a_count))

transformed_output = user_input.replace("Python", "JAVA")
print("I replaced word Python with JAVA: ")
print(transformed_output)