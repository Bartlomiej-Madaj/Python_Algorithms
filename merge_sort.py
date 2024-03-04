def merge(array, left_index, mid_index, right_index):
    left_array: list = array[left_index:mid_index+1]
    right_array: list = array[mid_index+1:right_index+1]

    array_index = left_index
    i = 0
    j = 0

    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            array[array_index] = left_array[i]
            i += 1
        else: 
            array[array_index] = right_array[j]
            j += 1
        array_index += 1     

    while i < len(left_array):
        array[array_index] = left_array[i]
        i += 1
        array_index += 1

    while j < len(right_array):
        array[array_index] = right_array[j]
        j += 1
        array_index += 1

def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return
    
    mid_index = left_index + int((right_index - left_index)/2)
    merge_sort(array, left_index, mid_index)
    merge_sort(array, mid_index+1, right_index)

    merge(array, left_index, mid_index, right_index)


