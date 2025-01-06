file = open("useValues2.txt", "a+")

while True:
    line = input("Write a value: ")
    if line == "CLOSE":
        file.close()
        break
    elif line == "SAVE":
        file.close()
        file = open("useValues2.txt", "a+")
    else:
        file.write(line + "\n")

