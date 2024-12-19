import datetime

def print_date():
    currDate = datetime.datetime.now()
    print(f"Today is {currDate.strftime("%A")}, "
          f"{currDate.strftime("%B")} "
          f"{currDate.strftime("%d")}, "
          f"{currDate.strftime("%Y")}.")

    # Shorter version
    print(datetime.datetime.now().strftime("Today is %A, %B %d, %Y"))

if __name__ == "__main__":
    print_date()
