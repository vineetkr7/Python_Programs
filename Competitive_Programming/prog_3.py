# Lexicographically largest array

# Problem Description

# Given an integer array A consisting of distinct elements.
# You are asked to create a lexicographically largest array S=X+reverse(Y) ('+' denotes concatenation) such that it satisfies the following conditions:
# • len(S) <= len(A)
# • X is the prefix array of array A and Y is the suffix array of array A.
# Note: Array X or Y can be empty.

# Problem Constraints

#     1 <= len(A) <= 10^5
#     1 <= A[i] <= 10^9

# Input Format

# First and only argument is an integer array Array.

# Output Format

# Return an integer array denoting lexicographically largest array S.

# Example Input                                                                       Example Output

# Input 1:                                                                            Output 1:
#   A = [4, 1, 3, 2]                                                                    [4, 2, 3, 1]

# Input 2:                                                                            Output 2:
#   A = [ 10, 20, 30, 40 ]                                                              [40, 30, 20, 10]

# Input 3:                                                                            Output 3:
#   A = [ 20, 69, 4, 83, 23, 100, 63, 50, 85, 53, 40, 44, 1 ]                           [20, 69, 4, 83, 23, 100, 63, 50, 85, 53, 40, 44, 1]


import ast

def solve(A):
    result_list = []
    for i in range(len(A), -1, -1):
        if i == 0:
            X = []
        else:
            X = A[0:i]
        if i == len(A):
            Y = []
        else:
            Y = A[i:]
            Y.reverse()
        num = int(''.join(str(s) for s in X + Y))
        result_list.append((X, Y, num))
    max_num = 0
    for item in result_list:
        if max_num < item[2]:
            max_num = item[2]
            X = item[0]
            Y = item[1]
    return X + Y

A = list(map(int, ast.literal_eval(input())))
print(solve(A))
