'''
문제: 자연수 n이 소수인지 아닌지를 출력하기

조건1: 반복문을 사용하여 주어진 숫자 n을 2부터 n-1까지 반복하면서 나누고,
       나눈 결과가 하나라도 나눈 몫을 구할 수 있으면 소수가 아닌 합성수이다.
조건2: 위의 반복문이 끝난 결과로 제어 변수가 주어진 n과 같으면 소수이고 같지 않으면 합성수이다.
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
    check_prime(19)
    check_prime(130)
    check_prime(37)
    check_prime(20)
    check_prime(21)    
