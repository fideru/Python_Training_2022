def array_ascend():
    array = [8, 6, 7, 2, 3, 0, 5, 4, 9, 1]
    temp = 0

    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    #                temp = array[i]
    #                array[i] = array[j]
    #                array[j] = temp
    return(array)

print(array_ascend())


#Just a testing line for the pull requests