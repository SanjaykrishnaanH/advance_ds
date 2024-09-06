"""
Kadane's algorithm is an efficient method used to find the maximum sum of a contiguous subarray 
within a one-dimensional array of numbers, which might include negative numbers. 
The algorithm runs in O(n) time complexity, making it very efficient for this problem.
"""

"""
Problem Statement

Given an array of integers, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
"""

def kadane_algorithm(arr):
    max_ending_here = arr[0]
    max_so_far = arr[0]

    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadane_algorithm(arr))  # Output: 6
