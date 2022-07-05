from array import array


def flatten(a):
    flat_array = []
    for n in a:
        if type(n) == list:
            flat_array += flatten(n)
        else:
            if n is not None:
                flat_array.append(n)
    return flat_array
