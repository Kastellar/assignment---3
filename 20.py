def dict_to_tuple(d: dict[str, int]) -> tuple:
    return tuple((k, v) for k, v in d.items())


d = {"a": 1, "b": 2, "c": 3, "d": 4}

print(dict_to_tuple(d))
