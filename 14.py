def often_element(lst: list[set]) -> set:
    return [lst[i - 1] & lst[i] for i in range(1, len(lst))][-1]


s1 = set("abcdf")
s2 = set("abef")
s3 = set("abghf")
s4 = set("abijf")

print(often_element([s1, s2, s3, s4]))
