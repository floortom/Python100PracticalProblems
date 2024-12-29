checklist = ["Portugal", "Germany", "Spain"]
checklist = [i + " \n" for i in checklist]
# print(checklist)

with open("countries_missing.txt", "r") as file:
    contents = file.readlines()
    file.close()

updatedList = sorted(contents + checklist)
# print(updatedList)

with open("countries_missing_fixed.txt", "w") as file:
    for i in updatedList:
        file.write(i)
    file.close()
