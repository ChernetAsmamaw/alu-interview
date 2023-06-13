#!/usr/bin/python3
'''How many units of water will be retained after it rains?'''

""" Steps:
    1. Get the hight of walls from the user as a list aka walls
    2. Initialize variables left and right
    3. Initialize variables to keep track of the max height
    4. Initialize result to keep the total water retained
    5. Start iterating till right and left meet
    6. which ever side has the smaller wall, move index from it
    7. On the current index, check if the wall > the max height
    8. If yes, update the max height
    9. If no, add to result current hight - max height
    10. Return result

"""

def rain(walls):
    '''Return: Integer indicating total amount of rainwater retained'''
        # walls is a list of non-negative integers 
        # Eg: [0, 1, 0, 2, 0, 3, 0, 4] -> 6

    if not walls:
        return 0

    left = 0
    right = len(walls) - 1
    
    left_max = walls[left]
    right_max = walls[right]

    result = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, walls[left])
            result += left_max - walls[left]
        else:
            right -= 1
            right_max = max(right_max, walls[right])
            result += right_max - walls[right]

    return result