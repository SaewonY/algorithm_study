'''
Longest Valid Parenthesis
https://leetcode.com/problems/longest-valid-parentheses/
'''

def solution(s):

    stack = [0]
    longest = 0
    
    for c in s:
        if c == "(":
            stack.append(0)
        else:
            if len(stack) > 1:
                val = stack.pop()
                stack[-1] += val + 2
                longest = max(longest, stack[-1])
            else:
                stack = [0]

    return longest

def solution2(s):

    dp, stack = [0] * (len(s) + 1), []

    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            if stack:
                p = stack.pop()
                dp[i+1] = dp[p] + i - p + 1
    return max(dp)

input = "())()"
print(solution(input))
