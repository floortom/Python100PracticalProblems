import string

with open("countries_raw.txt", "r") as file:
    contents = [i for i in file.readlines()]

noNewLine = [i.strip("\n") for i in contents]
noTop = [i for i in noNewLine if i != "Top of Page" and i != "" and i not in string.ascii_uppercase]

for country in noTop:
    print(country)
