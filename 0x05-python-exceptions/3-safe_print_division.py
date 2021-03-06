#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = int(a) / int(b)
        return c
    except ZeroDivisionError:
        print("Inside result: None")
        return None
    finally:
        print("Inside result: {:.1f}".format(c))
        