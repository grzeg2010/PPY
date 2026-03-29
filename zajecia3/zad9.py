def get_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for letter in text:
        if letter in vowels:
            yield letter

program = get_vowels("programowanie")
for i in program:
    print(i)