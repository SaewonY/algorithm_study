'''
조이스틱
https://programmers.co.kr/learn/courses/30/lessons/42860
'''

def solution(name):
    m = [min(ord(c) - ord("A"), ord("Z") - ord(c) + 1) for c in name]
    where = 0
    answer = 0
    while True:
        answer += m[where]

        m[where] = 0
        
        if sum(m) == 0:
            break

        left, right = 1, 1

        while m[where - left] <= 0:
            left += 1
        while m[where + right] <= 0:
            right += 1

        answer += left if left < right else right
        where += -left if left < right else right

    return answer

input = "JEROEN"
print(solution(input))