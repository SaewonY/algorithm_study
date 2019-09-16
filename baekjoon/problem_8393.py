'''
문제
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
'''

N = int(input())

assert 1 <= N <= 10000

result = int(N*(N+1)/2)
print(result)