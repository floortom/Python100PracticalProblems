import glob

for file in glob.iglob("subdirs/**/*.py", recursive=True):
    print(file)

print()
pyFiles = glob.glob("subdirs/**/*.py", recursive=True)
print(len(pyFiles))
