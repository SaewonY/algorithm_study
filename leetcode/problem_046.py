'''
Permutations
https://leetcode.com/problems/permutations/
'''

def solution(nums):

    length = len(nums)
    result = [num for num in list(permutations(nums, length))]
    return result

from itertools import permutations

input = [1, 2, 3]
print(solution(input))
