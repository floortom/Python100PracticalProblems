file = open("userValues.txt", "a+")

while True:
    line = input("Write a value: ")
    if line == "CLOSE":
        file.close()
        break
    else:
        file.write(line + "\n")
