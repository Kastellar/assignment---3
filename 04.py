def revers(lst, k):
    reversed_list = []
    for i in range(0, len(lst), k):
        group = lst[i:i+k]
        reversed_list.extend(reversed(group))
    return revers