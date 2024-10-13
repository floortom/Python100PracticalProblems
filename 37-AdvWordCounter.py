def word_count_adv(filepath):
    with open(filepath, "r") as file:
        string = file.read()
    spacesOnly = string.replace(",", " ")
    wordsList = spacesOnly.split(" ")
    return len(wordsList)

if __name__ == "__main__":
    print(word_count_adv("words2.txt"))
