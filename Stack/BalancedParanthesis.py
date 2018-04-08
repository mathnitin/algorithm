#!/bin/python

'''
Check for balanced parentheses in an expression

Given an expression string exp , write a program to examine whether the pairs and the orders of "{","}","(",")","[","]' 
are correct in exp. For example, the program should print true for exp = "[()]{}{[()()]()}" and false for exp = "[(])"
'''

if __name__ == "__main__":
    input = "[()]{}{[()()]()}"
    stack = []
    flag = True
    for char in input:
        if char == "[" or char == "{" or char == "(":
            stack.append(char)
        elif char == "}":
            if stack.pop() != "{":
                flag = False
                break
        elif char == ")":
            if stack.pop() != "(":
                flag = False
                break
        elif char == "]":
            if stack.pop() != "[":
                flag = False
                break
    print flag