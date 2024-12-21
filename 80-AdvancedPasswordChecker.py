while True:
    psw = input("Please type your new password. ")
    notes = []
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter.")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one digit.")
    if len(psw) < 5:
        notes.append("The password must be contain at least five characters.")
    if len(notes) == 0:
        print("the password is fine.")
        break
    if len(notes) != 0:
        print("Please check the following:")
        for note in notes:
            print(note)
        