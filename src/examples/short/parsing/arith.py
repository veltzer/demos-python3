#!/usr/bin/python3

# doing simple arithmetic evaluation in python

import pyparsing
import sys

number = pyparsing.Word(pyparsing.nums).setParseAction(lambda t: int(t[0]))


def number_act(s, loc, tok):
    return int(tok[0])
    # return 'foo'+tok[0]
number.setParseAction(number_act)

expr = pyparsing.Forward()
operand = number | expr

multop = pyparsing.oneOf('* /')
plusop = pyparsing.oneOf('+ -')
expr = pyparsing.operatorPrecedence(operand,
                                    [
                                    (multop, 2, pyparsing.opAssoc.LEFT),
                                    (plusop, 2, pyparsing.opAssoc.LEFT),
                                    ])


def expr_act(s, loc, tok):
    print('in here', s, loc, tok)
    if tok[0][1] == '*':
        return tok[0][0] * tok[0][2]
    if tok[0][1] == '/':
        return tok[0][0] // tok[0][2]
    if tok[0][1] == '+':
        return tok[0][0] + tok[0][2]
    if tok[0][1] == '-':
        return tok[0][0] - tok[0][2]
    return None
expr.setParseAction(expr_act)

expr.setDebug()

print(expr.parseString(sys.argv[1])[0])
