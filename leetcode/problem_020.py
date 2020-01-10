'''
Valid Parenthesis
https://leetcode.com/problems/valid-parentheses/
'''

def solution(s):

    if s == '':
        return True

    collected = []
    open_parenthesis = ['(', '{', '[']
    
    for string in s:
        if string in open_parenthesis:
            collected.append(string)

        if string not in open_parenthesis:
            if len(collected) == 0:
                return False
            temp = collected.pop()
            if temp == '(':
                if string != ')':
                    return False
            elif temp == '{':
                if string != '}':
                    return False
            elif temp == '[':
                if string != ']':
                    return False
    
    return True

input = "()[]{}"
print(solution(input))