'''
문제: 숫자 뒤집기

조건1: 정수의 자릿수를 계산 하는 방식을 고민해야 한다.
조건2: 이 문제의 경우는 반복문보다는 재귀 호출을 응용하는 것이 간단하다.
'''


# def flip_int(n):
#     n = int(str(n)[::-1])
#     return n

def solve(n):
    if n == 0:
        return 0
    print(n%10, end = ' ')
    solve(n//10)


if __name__ == '__main__':

    num = input("뒤집을 숫자를 입력하시오: ")
    # num = flip_int(num)
    # print(num)    
    solve(int(num))