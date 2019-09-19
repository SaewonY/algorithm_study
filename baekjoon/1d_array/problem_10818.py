'''
문제
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

출력
첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
'''

N = int(input())
if N not in range(10000000):
    exit()

num_list = list(map(int, input().split()))

max_num = num_list[0]
min_num = num_list[0]
for num in num_list:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(min_num, max_num)
