import string, os

letters = string.ascii_lowercase

if not os.path.exists("letters"):
    os.makedirs("letters")
for i in letters:
    filename = i + ".txt"
    # print(filename)
    with open("letters/" + filename, "w") as file:
        file.write(i)
        file.close()
