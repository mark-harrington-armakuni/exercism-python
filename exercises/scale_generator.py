"""
    # if starting_note ends in 'b' use flat scale
    # else use sharp scale
    # find index of starting note
    # get slice of chromatic sequence from starting note index to end of list
    # get remainder of sequence using start to starting note index - 1
    # append remainder to sequence
"""


def get_chromatic_from(starting_note):

    chromatic_sequence = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    if 'b' in starting_note:
        chromatic_sequence = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

    starting_note_index = chromatic_sequence.index(starting_note)

    complete_sequence = chromatic_sequence[starting_note_index:] + chromatic_sequence[:starting_note_index]

    return complete_sequence
