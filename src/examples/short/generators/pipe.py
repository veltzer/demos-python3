"""
Example of generators using generators
"""


def input_list():
    counter = 0
    while True:
        yield counter
        counter += 1
        if counter == 10:
            break


def square_it(input_generator):
    for x in input_generator():
        yield x ** 2


def main():
    result = []
    for x in square_it(input_list):
        result.append(x + 1)
    print(result)


main()
