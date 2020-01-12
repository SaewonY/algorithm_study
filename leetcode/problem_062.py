'''
Unique Paths
https://leetcode.com/problems/unique-paths/
'''

def solution(m, n):

    print(m, n)

    total = math.factorial(m+n-2)
    height = math.factorial(m-1)
    width = math.factorial(n-1)
    return int(total / (width * height))

import math

# total move you must take to the destination
# right == n-1, down == m-1 => total: m+n-2

m, n = 7, 3
print(solution(m, n))