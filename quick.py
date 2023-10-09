def quick_sort(u_list, first, last):
    if first < last:
        split_point = partition(u_list, first, last)

        quick_sort(u_list, first, split_point - 1)
        quick_sort(u_list, split_point + 1, last)


def partition(u_list, first, last):
    pivot = u_list[first]
    left_mark = first + 1
    right_mark = last
    done = False
    print(f'pivot = {pivot}')
    print(f'before while:   {u_list}')
    while done is not True:
        while left_mark <= right_mark and u_list[left_mark] <= pivot:
            left_mark += 1
        while pivot <= u_list[right_mark] and right_mark >= left_mark:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            u_list[left_mark], u_list[right_mark] = u_list[right_mark], u_list[left_mark]
    print(f'after while:    {u_list[:right_mark+1]}')
    u_list[first], u_list[right_mark] = u_list[right_mark], u_list[first]
    print(f'move pivot:     {u_list[:right_mark+1]}')
    return right_mark


unorderedList = [22, 1, 64, 12, 25, 11, 48]
quick_sort(unorderedList, 0, 6)
print(unorderedList)
