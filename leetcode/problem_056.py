'''
Merge Intervals
https://leetcode.com/problems/merge-intervals/
'''

def solution(intervals):

    out = []
    intervals.sort()
    for arr in intervals:
        if out and arr[0] <= out[-1][-1]:
            out[-1][-1] = max(out[-1][-1], arr[-1])
        else: out += [arr]
    return out

input = [[1,4],[4,5]]
print(solution(input))