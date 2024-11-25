import glob

letters = []
fileList = glob.glob("letters/*.txt")
for filename in fileList:
    with open(filename, "r") as file:
        content = file.read().strip()
    if content in "python":
        letters.append(content)

print(letters)
