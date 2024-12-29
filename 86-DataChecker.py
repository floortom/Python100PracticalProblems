checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open("countries_clean.txt", "r") as file:
    content = file.readlines()
    content = [i.strip("\n") for i in content]
file.close()

checklist = [i for i in checklist if i in content]
print(checklist)
