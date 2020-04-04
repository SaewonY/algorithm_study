'''
다트게임
https://programmers.co.kr/learn/courses/30/lessons/17682

입력 형식
점수|보너스|[옵션]으로 이루어진 문자열 3세트.
예) 1S2D*3T

- 점수는 0에서 10 사이의 정수이다.
- 보너스는 S, D, T 중 하나이다.
- 옵선은 *이나 # 중 하나이며, 없을 수도 있다.

출력 형식
3번의 기회에서 얻은 점수 합계에 해당하는 정수값을 출력한다.

입출력 예제
예제	dartResult	answer	설명
1	1S2D*3T	37	11 * 2 + 22 * 2 + 33
2	1D2S#10S	9	12 + 21 * (-1) + 101
3	1D2S0T	3	12 + 21 + 03
4	1S*2T*3S	23	11 * 2 * 2 + 23 * 2 + 31
5	1D#2S*3S	5	12 * (-1) * 2 + 21 * 2 + 31
6	1T2D3D#	-4	13 + 22 + 32 * (-1)
7	1D2S3T*	59	12 + 21 * 2 + 33 * 2
'''

def solution(dartResult):

    bonus = {'S':1, 'D':2, 'T':3}
    option = {'':1, '*':2, '#':-1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)

    for i in range(len(dart)):

        if i >= 1 and dart[i][2] == '*':
            dart[i-1] *= 2
        
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

import re
input = '1S2D*3T'
print(solution(input))