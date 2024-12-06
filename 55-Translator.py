d = dict(weather="clima", earth="terra", rain="chuva")

request = input("Enter word: ")

# if request in d.keys():
#     print(d[request])
# else:
#     print("We could not find that word.")

def vocabulary(word):
    try:
        return d[str.lower(word)]
    except KeyError:
        return "That word does not exist."

print(vocabulary(request))
