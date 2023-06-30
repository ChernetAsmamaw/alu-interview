#!/usr/bin/python3
"""Pascal's Triangle
    - Write a function that returns a list of lists of integers
    - Returns an empty list if n <= 0
    - You can assume n will be always an integer
    - In the following example, n = 4
        - 1
        - 1 1
        - 1 2 1
        - 1 3 3 1
    - Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]] {4 rows}
"""

def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s
       triangle of n
    """
    if n <= 0:
        return []
    pascal = [[1]]
    for i in range(n - 1):
        temp = [0] + pascal[-1] + [0]
        row = []
        for j in range(len(pascal[i]) + 1):
            row.append(temp[j] + temp[j + 1])
        pascal.append(row)
    return pascal
