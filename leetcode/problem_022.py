'''
generate parenthesis
https://leetcode.com/problems/generate-parentheses/
'''

def solution(n):
    def generate(p, left, right, parens=[]):
        if left:
            generate(p + '(', left-1, right)
        if right > left:
            generate(p + ')', left, right-1)
        if not right:
            parens += p,
        return parens
    return generate('', n, n,)


# dynamic programming
def solution(n):

    dp = [[] for i in range(n+1)]
    dp[0].append('')

    for i in range(n+1):

        for j in range(i):
            
            dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i-j-1]]

    return dp[n]
    

input = 3
print(solution(input))

