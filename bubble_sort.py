import random
import time


def bubble_sort(arr):
    swap_happend = True
    while swap_happend:
        swap_happend = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swap_happend = True
                arr[num], arr[num+1] = arr[num+1], arr[num]


if __name__ == '__main__':
    list = []
    input_n = input("정렬할 데이터의 수: ")
    for i in range(int(input_n)):
        list.append(random.randint(1, int(input_n)))
    print("<정렬 전>")
    print(list)

    start_time = time.time()
    bubble_sort(list)
    running_time = time.time() - start_time

    print("<정렬 후>")
    print(list)

    print("데이터의 크기: {}".format(int(input_n)))

# O(N**2)