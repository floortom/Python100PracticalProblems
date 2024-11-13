import string

with open("alphabet.txt", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")
