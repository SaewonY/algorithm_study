'''
종이접기
https://programmers.co.kr/learn/courses/30/lessons/62049

입출력 예
n	result
1	[0]
2	[0,0,1]
3	[0,0,1,0,0,1,1]
'''


def solution(n):

    answer = [0]
    
    for i in range(1, n):
        k = [1-j for j in answer]
        answer = answer + [0] + k[::-1]

    return answer


input = 3
print(solution(input))