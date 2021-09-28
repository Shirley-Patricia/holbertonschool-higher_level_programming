#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        a = [i / j for i, j in zip(my_list_1, my_list_2)]
        return a
    except TypeError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
