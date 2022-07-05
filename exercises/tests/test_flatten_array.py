from exercises.flatten_array import flatten


def test_flatten_array_flattens_single_level_array():
    assert flatten([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_flatten_array_flattens_single_level_array_with_nones():
    assert flatten([1, None, None, 5]) == [1, 5]


def test_flatten_array_flattens_double_level_array():
    assert flatten([1, [2, 3, None, 4], [None], 5]) == [1, 2, 3, 4, 5]


def test_flatten_array_flattens_triple_level_array():
    assert flatten([1, [2, 3, None, 4], [None], 5, [6, [7, None, 8]]]) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_flatten_array_flattens_empty_array():
    assert flatten([]) == []


def test_flatten_array_flattens_empty_multi_level_array():
    assert flatten([[], [], [[], []]]) == []



