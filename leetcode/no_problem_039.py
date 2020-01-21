'''
Combination Sum
https://leetcode.com/problems/combination-sum/
'''

def solution(candidates, target):


    result = []
    candidates.sort()

    def dfs(target, index, path):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(index, len(candidates)):
            
            print("i", i)
            print("path", path)
            print("candidates[i]", candidates[i])    
            print("target", target)        
            print()
            dfs(target - candidates[i], i, path + [candidates[i]])
        
    dfs(target, 0, [])
    
    return result


input = [2,3,6,7]
target = 7
print(solution(input, target)) 