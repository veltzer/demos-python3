#!/usr/bin/python3

num = int(raw_input('Please enter number of elements: '))
list = range(num)
for x in range(num):
    current = int(raw_input('Please enter element' + str(x) + ': '))
    if x % 2 == 0:
        if x == num - 1:
            list[x] = current
        else:
            list[x + 1] = current
    else:
        list[x - 1] = current
print(list)
