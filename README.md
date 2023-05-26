# 0-minimum_operations

**The Problem:**

In a text file, there is a single character H. Your text editor can execute only two 
operations in this file: Copy All and Paste. Given a number n, write a method that calculates 
the fewest number of operations needed to result in exactly n H characters in the file.

**_________________________________________________________________________________________________**

**Prototype:**         _def minOperations(n)_

Returns an integer
If n is impossible to achieve, return 0

**__________________________________________________________________________________________________**

**Example:**

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
