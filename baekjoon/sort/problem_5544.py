'''
리그
https://www.acmicpc.net/problem/5544

입력
첫째 줄에 팀의 수 N (2 ≤ N ≤ 100)가 주어진다. 다음 N(N-1)/2개 줄에는 각 경기의 결과가 주어진다. 
경기의 결과는 A B C D와 같이 네 개의 정수로 나타내며, A팀이 C점, B팀이 D점을 획득했음을 의미한다. 
A와 B는 항상 다르다. 한 경기의 결과가 여러 번 주어지는 경우는 없다.
'''



import sys
from collections import defaultdict
N = int(input())

team_dict = defaultdict(int)

num_match = int(N*(N-1) / 2)

for i in range(num_match):
    first_team, second_team, first_score, second_score = map(int, sys.stdin.readline().split())
    
    if first_score == second_score:
        team_dict[first_team] += 1
        team_dict[second_team] += 1
    elif first_score > second_score:
        team_dict[first_team] += 3
    else:
        team_dict[second_team] += 3

result = [[v, k] for k, v in sorted(team_dict.items(), key=lambda item: item[0])]

result.sort(reverse=True)

idx = 0
result[0].append(1)

for i in range(1, N):
    if result[i-1][0] == result[i][0]:
        result[i].append(result[i-1][2])
        idx += 1
    elif result[i-1][0] > result[i][0]:
        result[i].append(result[i-1][2] + 1 + idx)
        idx = 0

result.sort(key = lambda x: x[1])

for i in range(N):
    print(result[i][2])

