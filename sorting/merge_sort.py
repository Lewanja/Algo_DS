def merge(array):
    mid_index = len(array)//2
    left_array = array[0:mid_index]
    right_array = array[mid_index:]

    if len(left_array)==0:
        print(right_array)
    if len(right_array) == 0:
        print(left_array)

    index_left = index_right = 0
    result =[]
    while len(result) < len(left_array) + len(right_array):
        if left_array[index_left] <= right_array[index_right]:
            result.append(left_array[index_left])
            index_left += 1
        else:
            result.append(right_array[index_right])
            index_right += 1
        if index_right == len(right_array):
            result += left_array[index_left:]
            break
        if index_left == len(left_array):
            result += right_array[index_right:]
            break
    return result

def merge_sort(array):
    midpoint = len(array)//2
    return merge(
        left = merge_sort(array[:midpoint]),
        right = merge_sort(array[midpoint:])
    )

arr = merge(array = [9,8,7,6,99,1,4,6,9])
print(arr)