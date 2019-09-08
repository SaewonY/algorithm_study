import random
import time

def selection_sort(arr):

    start_marker = 0

    while start_marker < len(arr):
        for i in range(start_marker, len(arr)):        
            if arr[start_marker] > arr[i]:
                arr[start_marker], arr[i] = arr[i], arr[start_marker]
        start_marker += 1


if __name__ == '__main__':
    
    list = []
    input_n = input("정렬할 데이터의 수: ")
    for i in range(int(input_n)):
        list.append(random.randint(1, int(input_n)))
    print("<정렬 전>")
    print(list)

    start_time = time.time()

    selection_sort(list)

    running_time = time.time() - start_time
    print("<정렬 후>")
    print(list)

    print("데이터의 크기: {}".format(int(input_n)))
    print("소요 시간: {}".format(running_time))
