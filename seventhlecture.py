"""
Practice of testing, debugging, and exceptions and assertion statements in Python.
"""


# add exception to a function
def repetition_text():
    try:
        input_one = int(input("Type a number: "))
        input_two = int(input("Type the number of times you want to repeat the number: "))
        print(input_one * input_two)
    except ValueError:
        print("User input is not an integer.")


