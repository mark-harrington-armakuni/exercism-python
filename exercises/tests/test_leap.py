from exercises.leap import is_leap_year


def test_leap_returns_true_for_1996():
    assert is_leap_year(1996)


def test_leap_returns_false_for_1995():
    assert not is_leap_year(1995)


def test_leap_returns_false_for_1900():
    assert not is_leap_year(1900)


def test_leap_returns_false_for_2000():
    assert is_leap_year(2000)
