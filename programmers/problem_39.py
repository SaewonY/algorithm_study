'''
등굣길
https://programmers.co.kr/learn/courses/30/lessons/42898

격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다. 
집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.

제한사항
격자의 크기 m, n은 1 이상 100 이하인 자연수입니다.
m과 n이 모두 1인 경우는 입력으로 주어지지 않습니다.
물에 잠긴 지역은 0개 이상 10개 이하입니다.
집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않습니다.

입출력 예
m	n	puddles	    return
4	3	[[2, 2]]	4
'''

def solution(m, n, puddles):

    maps = [[0] * (m+1) for _ in range(n+1)]
    print(maps)

    maps[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                maps[i][j] = 0
            else:
                maps[i][j] = maps[i][j-1] + maps[i-1][j]

    return (maps[-1][-1]) % 1000000007

m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))