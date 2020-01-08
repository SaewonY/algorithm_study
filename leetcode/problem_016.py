'''
3sum closest
https://leetcode.com/problems/3sum-closest/
'''

def solution(arr, target):

    arr.sort()
    closest = 10000
    answer = 0

    for i in range(len(arr) - 2):
        
        l, r = i+1, len(arr)-1
    
        while l < r:
            total = arr[i] + arr[l] + arr[r]
            distance = abs(total - target)
            if distance < closest:
                closest = distance
                answer = total 
            if total == target:
                return target
            elif total < target:
                l += 1
            else:
                r -= 1

    return answer



# exactly one solution exists

input = [-1, 2, 1, -4]
target = 1
print(solution(input, target))
