import glob

letters = []
fileList = glob.glob("letters/*.txt")
# print(fileList)
for filename in fileList:
    with open(filename, "r") as file:
        letters.append(file.read().strip())
print(letters)
