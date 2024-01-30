def even_nums(lst: list[int]) -> set[int]:
    return set(i for i in lst if not i & 1)


lst = list(range(20))
print(even_nums(lst))
