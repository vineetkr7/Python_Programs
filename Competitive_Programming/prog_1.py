# Pair With Given Difference

# Problem Description

# Given a one-dimensional unsorted array A containing N integers.
# You are also given an integer B, find if there exists a pair of elements in the array whose difference is B.
# Return 1 if any such pair exists else return 0.

# Problem Constraints

#     1 <= N <= 105
#     -103 <= A[i] <= 103
#     -105 <= B <= 105

# Input Format

# First argument is an integer array A of size N.
# Second argument is an integer B.

# Output Format

# Return 1 if any such pair exists else return 0.

# Example Input                                                                       Example Output

# Input 1:                                                                            Output 1:
#   A = [5, 10, 3, 2, 50, 80]                                                            1
#   B = 78

# Input 2:                                                                            Output 2:
#   A = [ -259, -825, 459, 825, 221, 870, 626, 934, 205, 783, 850, 398 ]                 1
#   B = -42


import ast

def solve(A, B):
    for item in A:
        if abs(abs(item) - abs(B)) in A:
            return 1
    return 0  

A = list(map(int, ast.literal_eval(input())))
B = int(input())

print(solve(A, B))
