'''
Rotate Image
https://leetcode.com/problems/rotate-image/
'''

def solution(matrix):

    matrix[:] = zip(*matrix[::-1])
    # matrix[:] = [[nums[i] for nums in matrix[::-1]] for i in range(len(matrix))]
    
    return matrix

input = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

print(solution(input))