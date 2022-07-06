"""
    # if starting_note ends in 'b' use flat scale
    # else use sharp scale
    # find index of starting note
    # get slice of chromatic sequence from starting note index to end of list
    # get remainder of sequence using start to starting note index - 1
    # append remainder to sequence
"""


def get_chromatic_sequence(starting_note):

    chromatic_sequence = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    if 'b' in starting_note:
        chromatic_sequence = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

    starting_note_index = chromatic_sequence.index(starting_note)

    complete_sequence = chromatic_sequence[starting_note_index:] + chromatic_sequence[:starting_note_index]

    return complete_sequence


"""
    # Get chromatic sequence for starting note
    # Get length of Chromatic Sequence for Loop around check
    # Start Diatonic Sequence with Starting Note
    # Intialise Current Index
    # Iterate through chromatic sequence for intervals length
        # If next interval is m, get next note in chromatic sequence
        # Else if next interval is M get next note + 1 from chromatic sequence
        # Check and Fix Index for Loop Around Chromatic sequence

    # Return Diatonic Sequence
"""

def get_diatonic_sequence(starting_note, intervals):
    
    chromatic_sequence = get_chromatic_sequence(starting_note)

    chromatic_sequence_length = len(chromatic_sequence)
    
    diatonic_sequence = [starting_note]

    current_index = 0
    
    for i in intervals:
        if i == 'm':
            current_index += 1

        elif i == 'M':
            current_index += 2

        if current_index >= chromatic_sequence_length:
            current_index = current_index - chromatic_sequence_length
            
        diatonic_sequence.append(chromatic_sequence[current_index])

    return diatonic_sequence
