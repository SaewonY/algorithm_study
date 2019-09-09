def merge_sorted(arr1, arr2):
    # print("Merge function called with lists below:")
    # print(f"Left: {arr1} and right: {arr2}")
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
        # print(sorted_arr)
    
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr


def mergesort(arr):
    if len(arr) < 2:
        # print(f"Base condition reached with {arr[:]}")
        return arr[:]
    else:
        middle = len(arr)//2
        # print("Current list too work with:", arr)
        # print("Left split:", arr[:middle])
        # print("Right split:", arr[middle:])
        l1 = mergesort(arr[:middle])
        l2 = mergesort(arr[middle:])
        return merge_sorted(l1, l2)


############ Program Execution ###########

l = [8, 6, 2, 5, 2, 3, 8, 7, 2, 1]
# print(mergesort(l))

############ End Program ###########