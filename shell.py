def shell_sort(u_list):
    h = int(len(u_list) / 2)

    while h > 0:
        for start in range(h):
            sort(u_list, start, h)
        h = int(h/2)

def sort(u_list, start, gap):
    for i in range(start+gap, len(u_list), gap):
        currentValue = u_list[i]
        position = i

        while position >= gap and u_list[position - gap] > currentValue:
            u_list[position] = u_list[position - gap]
            position = position - gap


        u_list[position] = currentValue
    print(u_list)

unordered = [12, 53, 10, 25, 64, 23, 31, 44]
shell_sort(unordered)
print(unordered)