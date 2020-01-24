'''
숫자 야구
https://programmers.co.kr/learn/courses/30/lessons/42841

문제 설명
숫자 야구 게임이란 2명이 서로가 생각한 숫자를 맞추는 게임입니다.
각자 서로 다른 1~9까지 3자리 임의의 숫자를 정한 뒤 서로에게 3자리의 숫자를 불러서 결과를 확인합니다. 그리고 그 결과를 토대로 상대가 정한 숫자를 예상한 뒤 맞힙니다.

* 숫자는 맞지만, 위치가 틀렸을 때는 볼
* 숫자와 위치가 모두 맞을 때는 스트라이크
* 숫자와 위치가 모두 틀렸을 때는 아웃

예를 들어, 아래의 경우가 있으면
A : 123
B : 1스트라이크 1볼.
A : 356
B : 1스트라이크 0볼.
A : 327
B : 2스트라이크 0볼.
A : 489
B : 0스트라이크 1볼.
이때 가능한 답은 324와 328 두 가지입니다.

질문한 세 자리의 수, 스트라이크의 수, 볼의 수를 담은 2차원 배열 baseball이 매개변수로 주어질 때, 가능한 답의 개수를 return 하도록 solution 함수를 작성해주세요.

제한사항
질문의 수는 1 이상 100 이하의 자연수입니다.
baseball의 각 행은 [세 자리의 수, 스트라이크의 수, 볼의 수] 를 담고 있습니다.

입출력 예
baseball	                                            return
[[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]	2
'''

def baseball_fun(x, y):

    x = list(x)
    y = list(y)
    s, b = 0, 0
    
    for i in range(3):
        if x[i] in y:
            if y.index(x[i]) == i:
                s += 1
            else:
                b += 1
    return [s, b]


def solution(baseball):

    '''
    referece: https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%AB%EC%9E%90-%EC%95%BC%EA%B5%AC-in-python
    '''
    v = list(map(lambda x: str(x[0]), baseball)) # 질문하는 숫자
    r = list(map(lambda x: [x[1], x[2]], baseball)) # 질문에 대한 답

    all = list(itertools.permutations(range(1, 10), 3)) # 모든 가능한 수
    all = list(map(lambda x: list(map(str, x)), all))
    
    cnt = 0
    for x in all:
        if [baseball_fun(x, y) for y in v] == r:
            cnt += 1

    return cnt

import itertools

input = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
print(solution(input))

