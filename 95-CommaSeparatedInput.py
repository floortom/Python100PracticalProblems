line = input("Enter values separated by commas: ")
lineList = line.split(",")
print(lineList)

with open("userData.txt", "a+") as file:
    for i in lineList:
        file.write(i + "\n")
    file.close()
