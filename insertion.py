unorderedList = [64, 25, 12, 22, 11]


def insertion_sort(list):
    for index, element in enumerate(list[1:], 1):
        while index > 0 and element < list[index - 1]:
            list[index], list[index - 1] = list[index - 1], list[index]
            index -= 1
            print(list)
    return list


orderedList = insertion_sort(unorderedList)
