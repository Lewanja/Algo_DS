array = [2,5,3,6,8,2,99,2,5,6,1,8,0]

len_array = len(array)

for index_len_array in range(len_array):
    already_sorted= True
    for index_array in range(len_array - index_len_array -1 ):
        if array[index_array]>array[index_array + 1]:
            array[index_array], array[index_array+1] = array[index_array+1], array[index_array]
            already_sorted = False

    if already_sorted:
        break

    print(array)

# Reverse_order
def bubblesort(list):

# Swap the elements to arrange in order
   for iter_num in range(len(list)-1,0,-1):
      for idx in range(iter_num):
         if list[idx]>list[idx+1]:
            temp = list[idx]
            list[idx] = list[idx+1]
            list[idx+1] = temp
list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)