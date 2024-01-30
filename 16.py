# Write a function that takes a dictionary as input, where the keys are strings
# and the values are lists of integers. The function should return a new
# dictionary containing the same keys but with the values sorted in ascending
# order


def sort_values(d: dict[str, list[int]]) -> dict[str, list[int]]:
    return {k: sorted(v) for k, v in d.items()}


d = {"a": [2, 3, 1], "b": [4, 6, 5], "c": [9, 7, 8]}
print(sort_values(d))
