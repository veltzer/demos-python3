#!/usr/bin/python3

'''
Showing how to sort tuples in reverse
'''


def my_tup_revese(t1, t2):
    if (t1[1], t1[0]) < (t2[1], t2[0]):
        return -1
    if (t1[1], t1[0]) > (t2[1], t2[0]):
        return 1
    if (t1[1], t1[0]) == (t2[1], t2[0]):
        return 0


def my_revese(t1, t2):
    if t2 < t1:
        return -1
    if t2 > t1:
        return 1
    if t2 == t1:
        return 0


def my_first_cor_key(t):
    return t[1]


def by_y_x(t):
    return t[1], t[0]

mylist = [(1, 7), (2, 5), (0, 0), (3, 8), (1, 8), (2, 8)]
# lets see how regular sort works...
print(sorted(mylist))
# lets see how reverse works...
print(sorted(mylist, cmp=my_revese))
# lets see how second tuple co-ordinate sort works...
print(sorted(mylist, cmp=my_tup_revese))
# lets see how use the key function
print(sorted(mylist, key=my_first_cor_key))
# lets see how use the key function
print(sorted(mylist, key=by_y_x))
