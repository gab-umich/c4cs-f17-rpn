#!/usr/bin/env python3


import operator
import readline
import colored
from colored import stylize

addColor = colored.fg("red") + colored.attr("bold")
subColor = colored.fg("blue") + colored.attr("bold")
divColor = colored.fg("yellow") + colored.attr("bold")
mulColor = colored.fg("green") + colored.attr("bold")
powColor = colored.fg("white") + colored.attr("bold")
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            if token == '+':
                print(stylize("Added to: ", addColor))
            elif token == '-':
                print(stylize("Substracted to: ", subColor))
            elif token == '*':
                print(stylize("Multiplied to: ", mulColor))
            elif token == '/':
                print(stylize("Divided to: ", divColor))
            elif token == '^':
                print(stylize("Exponentiated to: ", powColor))
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)
        

if __name__ == '__main__':
    main()
