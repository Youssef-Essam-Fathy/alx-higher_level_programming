#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        my_list.insert(idx, element)
        return my_list
# print(new_in_list([1,2,3],1,4))
