def combine_dicts(d1: dict, d2: dict) -> dict:
    return d1 | d2


d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"d": 4, "e": 5, "f": 6}

print(combine_dicts(d1, d2))
