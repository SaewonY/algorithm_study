import random
import time

compare_counter = 0
swap_counter = 0

def insertion_sort(my_list):
    global compare_counter, swap_counter
    my_list.insert(0, -1)
    for s_idx in range(2, len(my_list)):
        temp = my_list[s_idx]
        ins_idx = s_idx
        compare_counter += 1
        while my_list[ins_idx-1] > temp:
            swap_counter += 1
            my_list[ins_idx] = my_list[ins_idx-1]
            ins_idx = ins_idx - 1

        my_list[ins_idx] = temp
    del my_list[0]

if __name__ == '__main__':
    list = []
    input_n = input("정렬할 데이터의 수: ")
    for i in range(int(input_n)):
        list.append(random.randint(1, int(input_n)))

    print("<정렬 전>")
    print(list)
    
    start_time = time.time()
    insertion_sort(list)
    running_time = time.time() - start_time

    print("<정렬 후>")
    print(list)

    print("데이터의 크기: {}".format(int(input_n)))
    print("비교 횟수: {}".format(compare_counter))
    print("교환 횟수: {}".format(swap_counter))
    print("실행 시간: {}".format(running_time))


# O(N**2)
        