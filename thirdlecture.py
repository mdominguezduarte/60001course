#Return the letter of a DNI
def letter_nie():
    dni = ""

    while len(dni) != 9 or dni[-1].isdigit() or not dni[0:7].isdigit():
        dni = input("Please input a DNI with eight digits and a letter at the end: ")

    print("The letter of your DNI is", dni[-1].capitalize())
