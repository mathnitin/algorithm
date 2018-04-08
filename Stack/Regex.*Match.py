#!/bin/python

'''
Implement regex match for . and * for pattern macthing.

If regex is a match it should print match if not print no-match.
'''

def findToken(regex = "ab*.d.*"):
    tokens = []                            
    stPoint = 0                            
    if regex[stPoint] == "*":
        return tokens
    while stPoint < len(regex) :
        if regex[stPoint].isalnum() == True:
            tokens.append(regex[stPoint])
            stPoint += 1
        elif regex[stPoint] == "*":
            tokens.append(tokens.pop()+"*")
            stPoint += 1
        elif regex[stPoint] == ".":
            if stPoint+1 == len(regex):
                tokens.append(".")
                stPoint += 1
            else:
                stPoint += 1
                if regex[stPoint] == "*":
                    tokens.append(".*")
                    stPoint += 1
                else:
                    tokens.append(".")
    return tokens

if __name__ == "__main__":
    input = "abbbbcde"
    regex = "ab*.d.*"

    # Flag used to decide it pattern matched or not.
    patternMatch = True
    # Index of input string
    index = 0

    # Fetch all tokens
    tokens = findToken(regex)

    try:
        print "input: ", input
        print "regex: ", regex
        for i in xrange(len(tokens)):
            token = tokens[i]
            #print token
            if token.isalnum() == True:
                # If token consits of only character or number. 
                if input[index] != token:
                    #print "1"
                    patternMatch = False
                    break
                else:
                    index += 1
            else:
                # If token contains '.' or '*'
                if len(token) == 1:
                    # If token is '.'
                    if index == len(input):
                        #print "2"
                        patternMatch = False
                        break
                    else:
                        index += 1
                else:
                    # If token is '(alnum)*' or '.*'
                    if str(token[0]).isalnum() == True:
                        # If token starts with alnum
                        if input[index] == token[0]:
                            while input[index] == token[0] and index < len(input):
                                index += 1
                        else:
                            #print "3"
                            patternMatch = False
                            break
                    else:
                        # If token is .*
                        if i != len(tokens)-1:
                            #print "4"
                            patternMatch = False
                            break
                        else:
                            if index == len(input):
                                #print "5"
                                patternMatch = False
                                break
                            index = len(input)
        if index != len(input) or i != len(tokens)-1:
            #print "6"
            patternMatch = False                    
    except IndexError:
        #print "7"
        patternMatch = False
    finally:
        if patternMatch == True:
            print 'Pattern matched.'
        else:
            print 'Pattern not matched.'