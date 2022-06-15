weight_lb = input('Cuanto pesas en libras?')
weight_kg = int(weight_lb) / 0.45
print('Tu peso en KG es ' + str(weight_kg))


def array_ascend():
    array = [8, 6, 7, 2, 3, 0, 5, 4, 9, 1]
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return(array)
