#!/usr/bin/python3


def minOperations(n):
    # Lets initialize a list to store the number of operations
    # ls will has a lenght of n+1 because we will start from 0
    ls = [0]*(n+1)
    # Since we already have one H in the editor, we will start from 2
    # Because number of opraions required to get 1 H is 0
    ls[1] = 0
    for i in range(2, n+1):
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
