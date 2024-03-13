array = [2,5,3,6,8,2,99,2,5,6,1,8,0]


for index in range(1,len(array)):
    key_item = array[index]
    position = index - 1

    while position >=0 and array[position]> key_item:
        array[position+1]= array[position]
        position -= 1
    array[position+1] = key_item

    print(array)