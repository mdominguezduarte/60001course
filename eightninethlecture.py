"""
Define different classes.
Different classes are defined to create a flashcard
"""
from varname import nameof

NAME_CARD = "Name Card"
NAME = "Name"
COURSE = "Course"
UNI_YEAR = "University"
QUARTER = "Quarter"


class Subject(object):
    def __init__(self, name, course, uni_year, quarter):
        self.name = name
        self.course = course
        self.uni_year = uni_year
        self.quarter = quarter

    # getters
    def get_name(self):
        return self.name

    def get_course(self):
        return self.course

    def get_uni_year(self):
        return self.uni_year

    def get_quarter(self):
        return self.quarter

    # setters
    def self_name(self, name):
        self.name = name

    def self_course(self, course):
        self.course = course

    def self_uni_year(self, uni_year):
        self.uni_year = uni_year

    def self_quarter(self, quarter):
        self.quarter = quarter

    def __str__(self):
        return "subject: " + str(self.name) + "course: " + str(self.course) + "university year" + str(
            self.uni_year) + "quarter: " + str(self.quarter)


class Cards(Subject):
    # init function
    def __init__(self, name_card, name, course, uni_year, quarter):
        Subject.__init__(self, name, course, uni_year, quarter)
        self.name_card = name_card
        self.self_name(name)
        self.self_course(course)
        self.self_uni_year(uni_year)
        self.self_quarter(quarter)

    # getter ans setter method
    def get_name_card(self):
        return self.name_card

    def self_name_card(self, name_card):
        self.name_card = name_card

    def len_variables(self, variable):
        len(variable)

        number = 50 - 10 - len(variable) - len(str(self.descrip_variables(variable)))
        return number

    def descrip_variables(self, variable):
        if variable == self.name_card:
            return NAME_CARD
        elif variable == str(self.uni_year):
            return UNI_YEAR
        elif variable == self.course:
            return COURSE
        elif variable == self.name:
            return NAME
        elif variable == self.quarter:
            return QUARTER
        else:
            return None

    def print_card(self):
        print(50 * "*" + "\n" + 50 * "*")

        print(2 * "*" + "   " + NAME_CARD + ": " + self.name_card + "   " + self.len_variables(self.name_card) * "*")

        print(2 * "*" + "   " + NAME + ": " + self.name + "   " + self.len_variables(self.name) * "*")

        print(2 * "*" + "   " + COURSE + ": " + self.course + "   " + self.len_variables(self.course) * "*")

        print(2 * "*" + "   " + UNI_YEAR + ": " + str(self.uni_year) + "   " + self.len_variables(str(self.uni_year)) * "*")

        print(2 * "*" + "   " + QUARTER + ": " + self.quarter + "   " + self.len_variables(
            self.quarter) * "*")

        print(50 * "*" + "\n" + 50 * "*")

    def __str__(self):
        return "subject: " + str(self.name) + "course: " + str(self.course) + "university year" + str(
            self.uni_year) + "quarter: " + str(self.course) + "Name_card:" + str(self.name_card)
