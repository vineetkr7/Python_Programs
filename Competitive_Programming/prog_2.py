# 3 Sum

# Problem Description

# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
# Return the sum of the three integers.
# Assume that there will only be one solution


# Input Format

# First argument is an integer array A.
# Second argument is an integer B.


# Output Format

# Return an integer array denoting lexicographically largest array S.


# Example Input                                                     Example Output

# Input 1:                                                          Output 1:
# A = [-10, -10, -10]                                                  -30
# B = -5

# Input 2:                                                          Output 2:
# A = [-1, 2, 1, -4]                                                    2
# B = 1

# Input 3:                                                          Output 3:
# A = [ 5, -20, -1, 5, 16, 18 ]                                         1
# B = 1


import ast

def threeSumClosest(A, B):
    if len(A) < 3:
        return -1
    diff = abs(A[0] + A[1] + A[2] - B)
    ans =  A[0] + A[1] + A[2]
    for i in range(len(A) - 2):
        for j in range(i+1, len(A) - 1):
            for k in range(j+1, len(A)):
                print(A[i], A[j], A[k], A[i]+A[j]+A[k])
                if (A[i] + A[j] + A[k]) == B:
                    ans = A[i] + A[j] + A[k]
                    break
                elif diff > abs(A[i] + A[j] + A[k] - B):
                    diff = abs(A[i] + A[j] + A[k] - B)
                    ans = A[i] + A[j] + A[k]
    return ans                    

A = ast.literal_eval(input())
B = int(input())

print(threeSumClosest(A, B))
