# Recursion and dictionaries

# power using iterative solution
import string


def power_iter(a, b):
    result = 1
    while b > 0:
        result *= a
        b -= 1
    return result


# power using recursion method
def power_iter_recursion(a, b):
    if b == 1:
        return a
    else:
        return a * power_iter_recursion(a, b - 1)


# power using iterative solution
def power_same_base(base, exponent1, exponent2, exponent3):
    result = 1
    exponent = exponent1 + exponent2 + exponent3
    while exponent > 0:
        result *= base
        exponent -= 1
        print("Loop... ")

    return result


# sum of exponents of the same base
def sum_exponents(exponent1, exponent2, exponent3):
    exponent = exponent1 + exponent2 + exponent3
    return exponent


# factorial recursividad
def factorial_rec(n):
    if n == 1:
        return 1
    else:
        return n * factorial_rec(n - 1)


# sum odd numbers
def sum_odd_number(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 1:
            element = n
        else:
            element = n - 1
    return element + sum_odd_number(element - 2)


# Alternative to Fibonacci function(How many rabbits do you have in one year if no one dies?
def population_rabbits(month):
    if month == 1 or month == 2:
        return 1
    else:
        return population_rabbits(month - 1) + population_rabbits(month - 2)


# A copy exercise done in class (This function is not created by myself)
def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ""
        for c in s:
            if c in "abscdefghijklmnopqrstuvwxyz":
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

#This is not a good practice for general coding.
"""
This is for nexted function practice
"""
def frequence_words(paragraph):
    def convert(paragraph):
        list_1 = list(paragraph.split(" "))
        return list_1
    def frequenc_word(list_1):
        myDict = {}
        for word in list_1:
            if word in myDict:
                myDict[word] += 1
            else:
                myDict[word] = 1
        return myDict
    return frequenc_word(convert(paragraph))

