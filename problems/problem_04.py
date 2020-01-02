'''
문제: 재귀 호출을 사용하여 n부터 1까지 출력하기

조건1: n부터 1까지 역순으로 화면에 출력해야 한다.
조건2: 출력하는 숫자가 1이 되면 프로그램을 종료한다.
'''

def print_to_n(n):
    if n >= 1:
        print(n)
        print_to_n(n-1)

if __name__ == '__main__':
    n = 10
    print_to_n(n)