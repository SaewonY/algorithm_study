'''
문제: 369 게임 만들기

조건1: 3의 배수를 확인하는 코드를 작성해야 한다.
조건2: 3의 배수가 아닌 경우는 숫자를 출력하고, 3의 배수인 경우는 "X"를 출력하는 코드를 작성해야 한다.
조건3: 사용자로부터 입력 받은 n까지 위의 과정을 반복해야 한다.
'''

def solve(n):
    i = 1
    while (i <= n):
        if i % 3 == 0:
            print("X ")
        else:
            print(i)
        i += 1

if __name__ == '__main__':
    solve(30)