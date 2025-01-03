while True:
    line = input("Write a value: ")
    if line == "CLOSE":
        break
    with open("userValues.txt", "a+") as file:
        file.write(line + "\n")
