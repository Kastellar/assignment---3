def unpack_tuples(tuple_list):
    first_elements = [t[0] for t in tuple_list]
    second_elements = [t[1] for t in tuple_list]
    third_elements = [t[2] for t in tuple_list]
    return first_elements, second_elements, third_elements
