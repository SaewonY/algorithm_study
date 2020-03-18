'''
Two Sum
https://leetcode.com/problems/two-sum/
'''

# first try
# class Solution:
#     def twoSum(self, nums: [], target: int) -> []:
#         answer = []
#         length = len(nums)
#         for i in range(length):
#             for j in range(i+1, length):
#                 if nums[i] + nums[j] == target:
#                     answer.append(i)
#                     answer.append(j)

#         return answer

# second try
class Solution:
    def twoSum(self, nums: [], target: int) -> []:
        
        dic = {}
        for i, num in enumerate(nums):
        
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i



input = [2, 7, 11, 15]
target = 9
S = Solution()
print(S.twoSum(input, target))