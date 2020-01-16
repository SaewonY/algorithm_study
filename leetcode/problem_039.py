'''
Combination Sum
https://leetcode.com/problems/combination-sum/
'''

def solution(nums, target):

    res = []
    nums.sort()
    def dfs(left, path, idx):
        if not left: res.append(path[:])
        else:
            for i, val in enumerate(nums[idx:]):
                if val > left: break
                dfs(left - val, path + [val], idx + i)
    dfs(target, [], 0)
    return res
    

input = [2, 3, 6, 7]
target = 7
print(solution(input, target))