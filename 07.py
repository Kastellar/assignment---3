def common_elements_tuples(tuple1, tuple2):
    common_elements = tuple(x for x in tuple1 if x in tuple2)
    return common_elements
