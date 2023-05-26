#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste.
    Given a number n, write a method that calculates the fewest number
    of operations needed to result in exactly n number of H characters
    in the file

    target_num
    - Target number of H we want the find the minimum operations for

    divider
    - Iterates over all possible divisors of the target number 'n' and
    check which ones are factors of 'n'. This is used to calculate the
    minimum number of operations required to reach 'n' by finding the
    sum of its factors.

    numOfOperations
    - The minimum number of operations required to reach 'n' from 1 H.
    """

    if n <= 1:
        return 0

    target_num = n
    divider = 2
    numOfOperations = 0

    while target_num > 1:
        if target_num % divider == 0:
            target_num = target_num / divider
            numOfOperations = numOfOperations + divider
        else:
            divider += 1
    return numOfOperations