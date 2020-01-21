'''
4Sum
https://leetcode.com/problems/4sum/
'''


def solution(nums, target):

    nums.sort()
    length = len(nums)

    collected = []

    for i in range(length-3):
        for j in range(i+1, length-2):
            

            first = nums[i]
            second = nums[j]
            left_idx, right_idx = j+1, length-1

            while left_idx < right_idx:
                total = first + second + nums[left_idx] + nums[right_idx]

                if total == target:
                    solution = [first, second, nums[left_idx], nums[right_idx]]
                    if solution not in collected:
                        collected.append(solution)
                
                if total < target:
                    left_idx += 1
                else:
                    right_idx -= 1
    
    return collected


# input = [1, 0, -1, 0, -2, 2]
input = [-3, -2, -1, 0, 0, 1, 2, 3]
target = 0
print(solution(input, target))