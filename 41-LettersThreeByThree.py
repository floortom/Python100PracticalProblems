import string

alphabet = string.ascii_lowercase + " "

with open("letters2.txt", "w") as file:
    for a, b , c in zip(alphabet[0::3], alphabet[1::3], alphabet[2::3]):
        file.write(a + b + c + "\n")
