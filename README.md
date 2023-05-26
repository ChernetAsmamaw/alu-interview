# Interview Prep: Minimum Operations Challenge

## What are mimimum operations? 
- Minimum operations, aka minimum steps or moves, refer to the smallest number of actions required to achieve a specific goal or outcome.       
- These actions can be any set of operations required to complete a task, such as copying, pasting, deleting, or moving elements. 
- Minimum operations are commonly used in various algorithms to find the most efficient way to solve a problem.
- Minimum operations work by analyzing the given problem and identifying the minimum number of steps required to achieve the desired outcome. 
  This involves breaking down the problem into smaller sub-problems and finding the optimal solution for each sub-problem.
- 

## Description of Problem

In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`.     
Given a number `n`, write a method that calculates the _fewest number of operations needed_ to result in exactly `n` `H` characters in the file.

* Prototype: `def minOperations(n)`
* Returns an integer
* If `n` is impossible to achieve, return `0`

### Example:

```
n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
```
