def swap(array, left_index, right_index):
    temp = array[left_index]
    array[left_index] = array[right_index]
    array[right_index] = temp

def get_pivot_and_swap(array, left_index, right_index):
    swap_index = left_index
    paviot = array[left_index]
    for i in range(left_index+1, right_index):
        if array[i] < paviot:
            swap_index += 1
            swap(array, swap_index, i)
    swap(array, left_index, swap_index)
    return swap_index

# Modify original array
def quick_sort_1(array, left_index, right_index):
    if left_index >= right_index:
        return
    pivot_index = get_pivot_and_swap(array, left_index, right_index)
    quick_sort_1(array, left_index, pivot_index)
    quick_sort_1(array, pivot_index+1, right_index)


# Doesn't modify original array and create new one
def quick_sort_2(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        left_arr = [i for i in array if i < pivot]
        right_arr = [i for i in array if i > pivot]
        return quick_sort_2(left_arr) + [pivot] + quick_sort_2(right_arr)

