
def countdown(n):
    print(n)
    if n <= 0:
        return
    else:
        countdown(n-1)

# countdown(4)
        
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

# print(fact(3))

my_list = [[[9, [8, 6, []]], [2, 4, [5, 6]]]]

def open(arr):
    for i in arr:
        if isinstance(i, list) and len(arr) > 0:
            open(i)
        else:
            print(i)

# open(my_list)


arr = [1,2,3,66,5,6,7]

def sum_arr(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_arr(arr[1:])

# print(sum_arr(arr))
    
def amount_of_num(arr):
    if len(arr) == 0:
        return 0
    return 1 + amount_of_num(arr[1:])

# print(amount_of_num(arr))
    

def max_num(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    sub_max = max_num(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

# print(max_num(arr))