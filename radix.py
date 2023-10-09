import math


def radix_sort(u_list):
    default_base = 10
    number_of_orders = int(math.log10(u_list[0])) + 1

    for j in range(number_of_orders):
        buckets = create_buckets(default_base)

        for number in u_list:
            digit = (number // (default_base ** j)) % default_base
            buckets[digit].append(number)

        u_list = [n for bucket in buckets for n in bucket]

    return u_list


def create_buckets(size):
    result = [[] for _ in range(size)]
    return result


unorderedList = [220, 540, 200, 120, 350, 400, 500]
orderedList = radix_sort(unorderedList)
print(orderedList)
