#!/usr/bin/python3
"""
This function calculates the minimum number of operations required to reach
a target number 'target_num' by finding all the integer values that 'target_num'
is divisible by and adding them together.

Parameters:
target_num (int): The target number to be reached.

Returns:
int: The minimum number of operations required to reach the target number.
"""


def min_operations(target_num):
        """This function finds the minimum number of operations
        required to obtain a length of H """

        if target_num <= 1:
            return 0
        divisor = 2
        sum_of_divisors = 0
        while divisor <= target_num:
            if target_num % divisor == 0:
                sum_of_divisors += divisor
                target_num = target_num / divisor
            else:
                divisor += 1
        return sum_of_divisors