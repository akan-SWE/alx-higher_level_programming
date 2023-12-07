#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    list_result = [True if not i % 2 else False for i in my_list]
    print(list_result)

    return list_result
