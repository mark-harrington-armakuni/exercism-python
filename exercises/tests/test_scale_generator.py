from exercises.scale_generator import get_chromatic_from


def test_return_sequence_starting_from_c():
    assert get_chromatic_from('C') == ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def test_return_sequence_starting_from_f_sharp():
    assert get_chromatic_from('F#') == ['F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F']


def test_return_sequence_starting_from_b_flat():
    assert get_chromatic_from('Bb') == ['Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A']
