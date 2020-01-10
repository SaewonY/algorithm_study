'''
Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
'''

# initial attempt
def solution(nums, target):

    length = len(nums)

    if not nums:
        return -1

    if nums[0] == target:
        return 0

    elif nums[0] > target:

        for i in range(length-1, 0, -1):
            # print(i)
            if nums[i] == target:
                return i
    else:
        for i in range(length):
            if nums[i] == target:
                return i
            

# optimized attempt (binary search)
def solution(nums, target):
    if not nums:
        return -1

    left, right = 0, len(nums) - 1

    while left <= right:
        
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


input = [4,5,6,7,0,1,2]
target = 7
print(solution(input, target))
