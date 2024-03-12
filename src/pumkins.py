def find_sum(our_list):
    n = len(our_list)
    ready_list = []
    for i in range(n):
        if i % 2 == 0:
            ready_list.extend(our_list[i])
        else:
            ready_list.extend(reversed(our_list[i]))
    return ready_list





