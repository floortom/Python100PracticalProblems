import string

alphabet = string.ascii_lowercase

with open("letters.txt", "w") as file:
    for i, j in zip(alphabet[0::2], alphabet[1::2]):
        file.write(i + j + "\n")
