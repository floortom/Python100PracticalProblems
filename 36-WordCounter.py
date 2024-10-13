def word_count(filepath):
    with open(filepath, "r") as file:
        string = file.read()
        print(string)
        wordList = string.split(" ")
        return len(wordList)

if __name__ == "__main__":
    print(word_count("words1.txt"))
