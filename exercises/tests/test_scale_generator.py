from exercises.scale_generator import get_chromatic_sequence, get_diatonic_sequence

def test_return_sequence_starting_from_c():
    assert get_chromatic_sequence('C') == ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def test_return_sequence_starting_from_f_sharp():
    assert get_chromatic_sequence('F#') == ['F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F']


def test_return_sequence_starting_from_b_flat():
    assert get_chromatic_sequence('Bb') == ['Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A']


def test_return_diatonic_sequence_starting_from_c():
    assert get_diatonic_sequence('C', 'MMmMMMm') == ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']


def test_return_diatonic_sequence_starting_from_f_sharp():
    assert get_diatonic_sequence('F#', 'MMmMMMm') == ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F', 'F#']


# def test_return_minor_scale_starting_from_c():
#     assert get_diatonic_sequence('C', 'MmMMmMM') == ['C', 'D', 'D#', 'F', 'G', 'Ab', 'Bb', 'C']
