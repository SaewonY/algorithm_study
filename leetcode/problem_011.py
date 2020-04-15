'''
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
'''

# brute force approach O(n**2)
def solution(height):
    print(height)
    maxArea = 0
    for i in range(len(height)-1):
        width = 1
        for j in range(i+1, len(height)):
            print(height[j])
            
            Area = min(height[i], height[j]) * width
            if Area > maxArea:
                maxArea = Area
            width += 1
    return maxArea

# two pointer approach O(n)
def solution(height):
    i, j = 0, len(height) - 1
    water = 0

    while i < j:
        water = max(water, (j - i) * min(height[i], height[j]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return water


input = [1,8,6,2,5,4,8,3,7]
print(solution(input))

