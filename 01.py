def merge_alternate(list1, list2):
    merged_list = []
    len1, len2 = len(list1), len(list2)
    max_len = max(len1, len2)

    for i in range(max_len):
        if i < len1:
            merged_list.append(list1[i])
        if i < len2:
            merged_list.append(list2[i])

    return merged_list

# Example usage:
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8, 9]
result = merge_alternate(list1, list2)
print(result)
