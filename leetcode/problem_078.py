'''
Subsets
https://leetcode.com/problems/subsets/
'''

def solution(nums):

    collected = []
    collected.append([])
    for i in range(1, len(nums)+1):
        temp = list(combinations(nums, i))
        for value in [list(value) for value in temp]:
            collected.append(value)
    return collected


def solution(nums):
    return [l for n in range(len(nums) + 1) for l in combinations(nums, n)]
     

from itertools import combinations

input = [1,2,3]
print(solution(input))