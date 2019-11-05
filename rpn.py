#!/usr/bin/env python3
import readline
from termcolor import colored

def calculate(arg):
    stack = list()
    for token in arg.split():
        # print(token)
        if token == '+':
            arg1 = stack.pop()
            arg2 = stack.pop()
            result = arg2 + arg1
            stack.append(result)
        elif token == '-':
                arg1 = stack.pop()
                arg2 = stack.pop()
                result = arg2 - arg1
                stack.append(result)
        elif token == '^':
            arg1 = stack.pop()
            arg2 = stack.pop()
            result = arg2 ** arg1
            stack.append(result)
        else:
            stack.append(int(token))
    if len(stack) != 1:
        raise TypeError("Malformed input")
    answer = stack.pop()
    if (answer < 0):
        print(colored(answer, 'red'))
    #else:
        #print(colored(answer, 'black'))
    print(answer)
    return answer

def main():
    while True:
        calculate(input("rpn calc> "))


if __name__ == '__main__':
    # Note: that's "underscore underscore n a m e ..."
    main()
