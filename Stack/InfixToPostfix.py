#!/bin/python
'''
Stack | Set 2 (Infix to Postfix)

Infix expression:The expression of the form a op b. When an operator is in-between every pair of operands.

Postfix expression:The expression of the form a b op. When an operator is followed for every pair of operands.

Why postfix representation of the expression?
The compiler scans the expression either from left to right or from right to left.

Consider the below expression: a op1 b op2 c op3 d
If op1 = +, op2 = *, op3 = +

The compiler first scans the expression to evaluate the expression b * c, then again scan the expression to add a to it. 
The result is then added to d after another scan.

The repeated scanning makes it very in-efficient. It is better to convert the expression to postfix(or prefix) form before evaluation.

The corresponding expression in postfix form is: abc*+d+. The postfix expressions can be evaluated easily using a stack. We will 
cover postfix expression evaluation in a separate post.

Algorithm
1. Scan the infix expression from left to right.
2. If the scanned character is an operand, output it.
3. Else,
   3.1 If the precedence of the scanned operator is greater than the precedence of the operator in the stack(or the stack is empty), 
   push it.
   3.2 Else, Pop the operator from the stack until the precedence of the scanned operator is less-equal to the precedence of the 
   operator residing on the top of the stack. Push the scanned operator to the stack.
4. If the scanned character is an '(', push it to the stack.
5. If the scanned character is an ')', pop and output from the stack until an '(' is encountered.
6. Repeat steps 2-6 until infix expression is scanned.
7. Pop and output from the stack until it is not empty.
'''

def infixToPostfix(input):
    precedence = {"+" : 1, "-" : 1, "*" : 2, "/" : 2, "^" : 3}
    output = ""
    operatorStack = []
    for char in input:
        # print "Char: ", char
        if char.isalpha() == True:
            # If  character is an operand, output it. 
            output += char
        else:
            # If character is an operator. 
            charPrec = 0
            if char == "(":
                # If the character is '(', push it to stack.
                operatorStack.append(char)
            elif char == ")":
                # If the character is ')', pop elements from stack till we hit '(' and append them to output.
                operator = operatorStack.pop()
                while operator != "(":
                    output += operator
                    if len(operatorStack) != 0:
                        operator = operatorStack.pop()
            else:
                # If the character is not '(' or ')'.

                # Find current character operator precedence. 
                charPrec = precedence[char]

                # Find the operator stack top most operand precedence.
                stackPrec = 0
                if len(operatorStack) > 0:
                    operator = operatorStack.pop()
                    if operator != '(':
                        stackPrec = precedence[operator]
                    operatorStack.append(operator)

                if charPrec > stackPrec:
                    # If the character precendence is greater than the precendence of the operator on stack,
                    #    or stack is empty. 
                    operatorStack.append(char)
                else: 
                    # Pop the operator from the stack until the precedence of the scanned operator is less-equal 
                    #     to the precedence of the operator residing on the top of the stack. Push the scanned operator 
                    #     to the stack.

                    # Make sure stack is not empty.
                    while len(operatorStack) != 0:
                        operator = operatorStack.pop()

                        # If we hit the '(', break out of loop.
                        if operator == "(":
                            operatorStack.append(operator)
                            break

                        stackPrec = precedence[operator]
                        # If the charcter precendence is less than or equal to the precedence of the operator in stack,
                        #     pop the operator from stack and append it to output string.
                        if charPrec <= stackPrec:
                            output += operator
                        else:
                            # Add the last poped operator back.
                            operatorStack.append(operator)
                            break

                    # Add the character to the stack.
                    operatorStack.append(char)

    # Add remaining operators to the output if any left.
    for operator in operatorStack:
        output += operator
    return output


if __name__  == "__main__":
    infixExp = "a+b*(c^d-e)^(f+g*h)-i"
    postfixExp = ""
    print "Input:  ", infixExp
    print "Output: ", infixToPostfix(infixExp)
