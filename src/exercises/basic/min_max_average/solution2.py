#!/usr/bin/python3


def my_min(list):
    min = list[0]
    for x in list:
        if x < min:
            min = x
    return min


def my_max(list):
    max = list[0]
    for x in list:
        if x > max:
            max = x
    return max


def my_sum(list):
    sum = 0
    for x in list:
        sum += x
    return sum


def min_max_avg(list):
    return my_min(list), my_max(list), float(my_sum(list)) / len(list)

print(min_max_avg(range(0, 100000)))
