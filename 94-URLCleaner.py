with open("urls.txt", "r+") as file:
    urls = [i.strip("\n") for i in file.readlines()]

urls = [i.replace("s", "", 1) for i in urls]
urls = [i[:5] + "/" + i[5:] for i in urls]
print(urls)
file.close()

with open("urlsCorrected.txt", "w") as file:
    for url in urls:
        file.write(url + "\n")
    file.close()
