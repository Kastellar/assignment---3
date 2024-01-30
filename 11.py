def combine(s1: set, s2: set) -> list[set]:
    """Returns intersection, union, difference"""
    return (s1.intersection(s2), s1.union(s2), s1.difference(s2))


s1 = set("abcdef")
s2 = set("defghi")

print(combine(s1, s2))
