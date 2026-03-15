print("Napisz jakieś zdanie: ")
sentence = str(input())

print("Długość: " + str(len(sentence)))
print("Zamiana spacji na _: " + sentence.replace(" ", "_"))

words_list = sentence.split(" ")
print(words_list)

print(sentence[0:3])
print(sentence[-4:])