def merge_sort(u_list):
    if len(u_list) > 1:
        middle = len(u_list)//2
        left = u_list[:middle]
        right = u_list[middle:]

        merge_sort(left)
        merge_sort(right)

        left_index = right_index = list_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                u_list[list_index] = left[left_index]
                left_index += 1
            else:
                u_list[list_index] = right[right_index]
                right_index += 1

            list_index += 1

        while left_index < len(left):
            u_list[list_index] = left[left_index]
            left_index += 1
            list_index += 1

        while right_index < len(right):
            u_list[list_index] = right[right_index]
            right_index += 1
            list_index += 1


unorderedList = [64, 25, 12, 22, 11]
merge_sort(unorderedList)
print(unorderedList)