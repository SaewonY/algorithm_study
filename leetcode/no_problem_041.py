'''
First Missing Positive
https://leetcode.com/problems/first-missing-positive/
'''


def solution(nums):


    '''
    solution
    https://leetcode.com/problems/first-missing-positive/discuss/17080/Python-O(1)-space-O(n)-time-solution-with-explanation
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within the range [1,...,l+1] 
    '''

    N = len(nums)
    nums.append(0)

    for i in range(N):
        if nums[i] < 0 or nums[i] >= N:
            nums[i] = 0

    for i in range(N):
        nums[nums[i]%N] += N
    for i in range(N):
        if nums[i] // N == 0:
            return i
    return N


input = [1,2,0]
print(solution(input))