#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l = "Last digit of"
if number >= 0:
    l_d = number % 10
else:
    l_d = abs(number) % 10 * -1
if l_d > 5:
    print("{} {} is {} and is greater than 5".format(l, number, l_d))
elif l_d == 0:
    print("{} {} is {} and is 0".format(l, number, l_d))
else:
    print("{} {} is {} and is less than 6 and not 0".format(l, number, l_d))
