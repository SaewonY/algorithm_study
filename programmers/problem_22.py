'''
팰린드롬 숫자

문제 설명
앞에서부터 읽을 때와 뒤에서부터 읽을 때 똑같은 단어를 팰린드롬(palindrome)이라고 합니다. 예를들어서 racecar, 10201은 팰린드롬 입니다.
두 자연수 n, m이 매개변수로 주어질 때, n 이상 m 이하의 자연수 중 팰린드롬인 숫자의 개수를 return 하도록 solution 함수를 완성해 주세요.

제한사항
m은 500,000이하의 자연수이며, n은 m 이하의 자연수입니다.

입출력 예
n	m	result
1	100	18
100	300	20
'''

def solution(n,m):
    count = 0
    for num in range(n, m+1):
        string_num = str(num)
        if num == int(string_num[::-1]):
            count += 1
    return count