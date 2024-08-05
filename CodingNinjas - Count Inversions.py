from os import *
from sys import *
from collections import *
from math import *

count=0

def mergesort(arr):
    global count
    if len(arr)<=1:
        return arr
    lefthalf=arr[:len(arr)//2]
    righthalf=arr[len(arr)//2:]
    leftsrt = mergesort(lefthalf)
    rightsrt = mergesort(righthalf)
    i=0
    j=0
    merged=[]
    while i<len(leftsrt) and j<len(rightsrt):
        if leftsrt[i]<=rightsrt[j]:
            merged.append(leftsrt[i])
            i+=1
        else:
            merged.append(rightsrt[j])
            j+=1
            count+=len(leftsrt)-i
    
    while i<len(leftsrt):
        merged.append(leftsrt[i])
        i+=1
    
    while j<len(rightsrt):
        merged.append(rightsrt[j])
        j+=1
    
    return merged

def getInversions(arr, n) :
    mergesort(arr)
    return count

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))
