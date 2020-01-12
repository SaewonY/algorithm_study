'''
Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
'''


# accumulation!!

def solution(nums):

    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
        return max(nums)

from itertools import accumulation

def solution(nums):
    return max(accumulation(nums, lambda x, y: x+y if x > 0 else y))


input = [-1,0,-2]
print(solution(input))