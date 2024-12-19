import datetime

age = int(input("Please share your current age."))

def calculate_birthyear(age):
    birthYear = datetime.datetime.now().year - age
    answer = f"I think you were born in {birthYear}."
    return answer

if __name__ == "__main__":
    print(calculate_birthyear(age))
