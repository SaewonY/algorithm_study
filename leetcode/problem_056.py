'''
Merge Intervals
https://leetcode.com/problems/merge-intervals/
'''

def solution(intervals):

    out = []

    intervals.sort()

    for arr in intervals:
        print("arr", arr)

        if out and arr[0] <= out[-1][-1]:
            out[-1][-1] = max(out[-1][-1], arr[-1])

        else: out += [arr]
        
        print(out)
    
    return out

# input = [[1,4], [4,8], [8,13], [14,19], [19, 21]]
# input = [[2,3],[4,5],[6,7],[8,9],[1,10]]

input = [[1,4],[4,5]]

print(solution(input))