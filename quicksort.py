arr = [1,75,3,66,5,20,7]


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [item for item in array if item < pivot]
        greater = [item for item in array if item > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)
    
# print(quicksort(arr))

test_list = [4, 6,1,7,3,2,5]

def get_pivot(array, pivot_index, right_index):
    pivot = array[pivot_index]
    swap = pivot_index
    for i in range(pivot_index+1, right_index):
        if array[i] < pivot:
            swap +=1
            temp = array[i]
            array[i] = array[swap]
            array[swap] = temp
    array[pivot_index] = array[swap]
    array[swap] = pivot
    return swap

def quicksort_2(array, left_index, right_index):
    if left_index >= right_index:
        return
    pivot_index = get_pivot(array, left_index, right_index)
    quicksort_2(array, left_index, pivot_index)
    quicksort_2(array, pivot_index+1, right_index)

#print(test_list)
#quicksort_2(test_list,  0, len(test_list))
#print(test_list)

def swap(array, left_index, right_index):
    temp = array[left_index]
    array[left_index] = array[right_index]
    array[right_index] = temp

def get_paviot_and_swap(array, left_index, right_index):
    swap_index = left_index
    paviot = array[left_index]
    for i in range(left_index+1, right_index):
        if array[i] < paviot:
            swap_index += 1
            swap(array, swap_index, i)
    swap(array, left_index, swap_index)
    return swap_index

def quick_sort_3(array, left_index, right_index):
    if left_index >= right_index:
        return
    paviot_index = get_paviot_and_swap(array, left_index, right_index)
    quick_sort_3(array, left_index, paviot_index)
    quick_sort_3(array, paviot_index+1, right_index)

#print(test_list)
#quick_sort_3(test_list, 0, len(test_list))
#print(test_list)

def quick_sort_4(array):
    if len(array) < 2:
        return array
    else:
        paviot = array[0]
        left_arr = [i for i in array if i < paviot]
        right_arr = [i for i in array if i > paviot]
        return quick_sort_4(left_arr) + [paviot] + quick_sort_4(right_arr)

# print(test_list)
# print(quick_sort_4(test_list))
# print(test_list)
