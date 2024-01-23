def common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_set = set1.intersection(set2)
    result_list = sorted(list(common_set))
    return result_list

result = common_elements(list1, list2)
print(result)
