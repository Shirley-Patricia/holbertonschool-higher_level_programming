#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list == []:
        return None
    my_list.sort()
    add = my_list[0]
    for i in range(0, (len(my_list)-1)):
        if my_list[i] != my_list[i + 1]:
            add += my_list[i + 1]
    return add
