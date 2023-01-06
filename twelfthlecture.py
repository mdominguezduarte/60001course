"""
Example of searching and sorting from 60001 Harvard course
"""


def search_sorted_list(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def return_msg(name_func, L, e):
    is_found = "It's not found"
    if name_func(L, e):
        is_found = f"{e} is found"
    return is_found


# the following function is not the same as the one from the course

def linear_search_unsorted(L, e):
    for i in range(len(L)):
        if e == L[i]:
            return True
    return False



