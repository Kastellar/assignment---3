def set_diff(s1: set, s2: set) -> tuple[set]:
    return (s1.difference(s2), s1.symmetric_difference(s2))


s1 = set("abcdef")
s2 = set("defghi")
print(set_diff(s1, s2))
