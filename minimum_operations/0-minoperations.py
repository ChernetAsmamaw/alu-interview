#!/usr/bin/python3
''' This program finds the minimum number of
operations required to get n number of H'''


def min_operations(n):
    """
    This function finds the minimum number of operations required to
    obtain a string of length 'n' consisting of the character 'H'
    using the following operations:
    1. Print one 'H'
    2. Select all 'H's
    3. Copy the selected 'H's
    4. Paste the copied 'H's
    
    Parameters:
    n (int): The target number of 'H's in the final string.
    
    Returns:
    int: The minimum number of operations required to obtain a string
     of length 'n'.
    """
    # Initialize a list to store the number of operations
    # The list will have a length of n+1 because we start from 0
    ops = [0] * (n + 1)
    
    for i in range(2, n + 1):
        # Find the smallest divisor for i
        for j in range(2, i + 1):
            if i % j == 0:
                # If i is divisible by j, we can obtain 'i' 'H's by performing
                # the minimum operations required for 'j' 'H's and then
                # multiplying by i // j (copy-pasting the 'j' 'H's (i // j) - 1 times).
                ops[i] = ops[j] + (i // j)
                break
    
    return ops[n]