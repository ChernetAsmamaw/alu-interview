#!/usr/bin/python3
''' This program finds the minimum number of
operations required to get n number of H'''

def minOperations(n):
    ''' This function finds the minimum number of operations'''
    # Lets initialize a list to store the number of operations
    # ls will has a length of n+1 because we will start from 0
    # n: represents the target number of H we want to get
    # ls: is a lis of length n+1 that stores the number of ops required
    # j: is any
    ls = [0]*(n+1)
    for i in range(2, n+1):
        # Since we already have one H in the editor, we will start from 2
        # Because number of opraions required to get 1 H is 0
        if n <= 1:
            return 0
        # Since number of max-op required is to copy & paste i 1 time
        # So we will initialize the value of ls[i] to i
        ls[i] = i
        # Now we will check if i is divisible by any number (j) from 2 to i-1
        # If yes, then we will copy & paste the number of times
        for j in range(2, i):
            if i % j == 0:
                # This is the min number of opes required to get i number of H
                ls[i] = ls[j] + (i//j)
    # Here we return the number of opes required to get n number of H
    return ls[n]