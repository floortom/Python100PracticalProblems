d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

print(d.items())

for key, value in d.items():
    print(f"{key} has value of {value}")
