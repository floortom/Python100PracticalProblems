def split_string(string):
    stringList = string.split(" ")
    return len(stringList)


if __name__ == "__main__":
    testString = "I like trains"
    print(split_string(testString))
