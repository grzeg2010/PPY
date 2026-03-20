# Napisz program zarządzający listą użytkowników.
# Program powinien:
# • przechowywać nazwy użytkowników,
# • umożliwić dodawanie nowych użytkowników,
# • sprawdzać czy dany użytkownik już istnieje,
# • umożliwić wyszukiwanie użytkowników,
# • wyświetlić listę użytkowników w uporządkowanej formie.
# Dodatkowo program powinien:
# • wyświetlić wybraną część listy użytkowników,
# • znaleźć użytkownika o najdłuższej nazwie.

users = set()

def add_user(user_name):
    if not does_user_exist(user_name):
        users.add(user_name)
        print("User added: " + user_name)
    else:
        print("[WARN] User " + user_name + " already exists!")

def does_user_exist(user_name):
    return user_name in users

def print_users_list(reverse_list):
    print(sorted(users, reverse=reverse_list))

add_user("Adam")
add_user("Auwuvuevuevue anietu vuevuevue uguemuguem osas")
add_user("Bartek")
add_user("Adam")
add_user("Antek")

print_users_list(False)
print("Odwrócona:")
print_users_list(True)

print("Od 1 do 2 użytkownika: " + str(sorted(users)[0:2]))
print("Najdłuższe imię: " + str(max(users, key=len)))