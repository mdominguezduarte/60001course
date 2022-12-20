# branching and iteration
import random


def test_one():
    x = 10
    # '/' insert automatically a space for you
    print("My fav num is", str(x) + ".", "X =", x)


# Type a number of times a number
def repetition_text():
    input_one = int(input("Type a number: "))
    input_two = int(input("Type the number of times you want to repeat the number: "))
    print(input_one * input_two)


# guess a number
def conditions():
    input_number = int(input("Input an integer number until 10: "))
    random_number = random.randint(1, 10)

    while (input_number != random_number):
        input_number = int(input("Input again an integer number until 10: "))

    print("You guessed the random number:", random_number)
    print(30 * "*", "END", 30 * "*")


# print a range of numbers from 1 to 100
def number_and_ranges():
    for n in range(100):
        for r in range(100):
            print(n, r+1)


#print multiplied element
def mul_numbers():
    mymul = 1
    for i in range(1,10,2):
        mymul *= i
        print(mymul)
