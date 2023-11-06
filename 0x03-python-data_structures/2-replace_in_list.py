#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
ml = [1,2,3]
i = 1
ne = 8
nl = replace_in_list(ml,i,ne)
print(nl)
print(ml)
