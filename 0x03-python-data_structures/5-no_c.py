#!/usr/bin/python3


def no_c(my_string):
    str_list = list(my_string)
    for i in range(len(str_list)):
        if str_list[i] == 'c':
            str_list[i] = ''
    modified_str = ''.join(str_list)
    return modified_str
