'''
문제: 2와 N 사이의 모든 소수를 출력하기

조건1: 2부터 N까지의 반복문으로 소수 확인 함수를 출력한다.
'''

def check_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            break
        i += 1

    if i == n:
        print("{}은 소수".format(n))
    else:
        print("{}은 합성수".format(n))



if __name__ == '__main__':
    i = 0
    while i < 20:
        check_prime(i)
        i += 1