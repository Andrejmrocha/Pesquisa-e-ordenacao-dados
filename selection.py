def selection_sort(list):
    size = len(list)
    for i in range(size - 1, -1, -1):
        max_index = i
        for j in range(i):
            if list[j] > list[max_index]:
                max_index = j

        if max_index != i:
            list[i], list[max_index] = list[max_index], list[i]
        print(list)

    return list


unorderedList = [64, 25, 12, 22, 11]
orderedList = selection_sort(unorderedList)
