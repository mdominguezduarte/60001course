import sys
import math


# Return the letter of a DNI
def letter_nie():
    dni = ""

    while len(dni) != 9 or dni[-1].isdigit() or not dni[0:7].isdigit():
        dni = input("Please input a DNI with eight digits and a letter at the end: ")

    print("The letter of your DNI is", dni[-1].capitalize())


# count the number of vowel letters
def number_vowels():
    print(20 * "*", "Welcome to count vowels of a string", 20 * "*")
    input_string = input("Please insert a string:")
    number_a = 0
    number_e = 0
    number_i = 0
    number_o = 0
    number_u = 0
    for char in input_string:
        if char == 'a' or char == 'A':
            number_a += 1

        elif char == 'e' or char == 'E':
            number_e += 1

        elif char == 'i' or char == 'I':
            number_i += 1

        elif char == 'o' or char == 'O':
            number_o += 1

        elif char == 'u' or char == 'U':
            number_u += 1

        else:
            continue

    print("A appears", number_a, 'times')
    print("E appears", number_e, 'times')
    print("I appears", number_i, 'times')
    print("O appears", number_o, 'times')
    print("U appears", number_u, 'times')


# check if the sequence is a nitrogenous base
def sequence_base():
    nitrogenousbase = "atgcuATUGC"
    sequence = input("Hello. Please insert a sequence: ")
    for char in sequence:
        if char in nitrogenousbase:
            print(char, "is a nitrogenous base.")

        else:
            sys.exit(char + " is not a nitrogenous base.")

    print(sequence, "is a nitrogenous base sequence.")


# pythagoras theorem limited to integer number
# c1 **2 + c2**2 = h** 2

def pitagoras_theorem():
    h = int(input("Insert the integer value of the hypotenuse:"))
    h_abs = abs(h)
    while h_abs < 2:
        h = int(input("Please,insert a bigger integer value of the hypotenuse:"))
        h_abs = abs(h)
    for c1 in range(1, h_abs + 1):
        if c1 ** 2 < h_abs ** 2:
            c2_cuadrado = h_abs ** 2 - c1 ** 2
            c2 = math.sqrt(c2_cuadrado)
            if c2.is_integer():
                print(f"The leg C1:{int(c1)}, the leg C2:{int(c2)} and the hypotenuse:{int(h_abs)} match the theorem.")
                break
            else:
                print("Searching...")

    print("The search is finished.")
