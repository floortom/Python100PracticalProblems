import string
import random

def generate_password():
    charSet = string.printable
    pswrdChars = random.sample(charSet, 6)
    pswrd = "".join(pswrdChars)
    return pswrd

if __name__ == "__main__":
    print(generate_password())
