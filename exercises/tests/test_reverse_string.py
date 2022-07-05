from exercises.reverse_string import reverse


def test_reverse_string_reverses_stringl():
    assert reverse('cool') == 'looc'


def test_reverse_string_reverses_empty_string():
    assert reverse('') == ''


def test_revers_string_reverses_single_character():
    assert reverse('s') == 's'
