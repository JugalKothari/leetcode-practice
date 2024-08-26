from os import *
from sys import *
from collections import *
from math import *


def sortedInsert(stack, current):
    if not stack or current>=stack[-1]:
        stack.append(current)
        return
    
    top=stack[-1]
    stack.pop()

    sortedInsert(stack, current)

    stack.append(top)


def sortStack(stack):
    # given data structure is a python list 
    # as list have all the similar operations available so use them
    # Write your code here
    if len(stack)==0:
        return

    top=stack[-1]
    stack.pop()

    sortStack(stack)

    sortedInsert(stack, top)
