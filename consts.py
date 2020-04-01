T = 2**(1/12)


def sign(x): return 1 if x > 0 else 0 if x == 0 else -1


''' for Note '''


# natural note numbers (midi encoding numbers), C=0, D=2, E=4, F=5, G=7, A=9, B=11
NATURAL_NNS = [0, 2, 4, 5, 7, 9, 11]


# 12 notes' names, only natural notes are shown
NOTE_NAMES = ['C', '', 'D', '', 'E', 'F', '', 'G', '', 'A', '', 'B']


''' for Interval '''


# axis 0: delta_nn, axis 1: delta_step, e.g. (delta_nn, delta_step) = (0, 0) ==> P1
INTERVAL_TYPES = [
    ['P', 'd', '!', '!', '!', '!', '!'],
    ['A', 'm', '!', '!', '!', '!', '!'],
    ['!', 'M', 'd', '!', '!', '!', '!'],
    ['!', 'A', 'm', '!', '!', '!', '!'],
    ['!', '!', 'M' ,'d' ,'!' ,'!' ,'!'],
    ['!', '!', 'A' ,'P' ,'!' ,'!' ,'!'],
    ['!', '!', '!' ,'A' ,'d' ,'!' ,'!'],
    ['!', '!', '!' ,'!' ,'P' ,'d' ,'!'],
    ['!', '!', '!' ,'!' ,'A' ,'m' ,'!'],
    ['!', '!', '!' ,'!' ,'!' ,'M' ,'d'],
    ['!', '!', '!' ,'!' ,'!' ,'A' ,'m'],
    ['!', '!', '!' ,'!' ,'!' ,'!' ,'M']
]


''' for DiatonicScale '''


# these two encoders are used to calculate number of accidentals
SCALE_TYPE_ENCODER = {'Locrian': -3, 'Phrygian': -2, 'Aeolian': -1, 'Dorian': 0, 'Mixolydian': 1, 'Ionian': 2, 'Lydian':3}

TONIC_NAME_ENCODER = {'F': -3, 'C': -2, 'G': -1, 'D': 0, 'A': 1, 'E': 2, 'B': 3}

# for `get_name` method
SCALE_TYPE_DECODER = ['Locrian', 'Phrygian', 'Aeolian', 'Dorian', 'Mixolydian', 'Ionian', 'Lydian']


''' for AlteredDiatonicScale '''


# get interval vectors of all 66 classes
INTERVAL_VECTOR_LIST = []
with open('all_heptatonic_scale_intervals.txt', 'r') as f:
    for line in f:
        INTERVAL_VECTOR_LIST.append(eval(line))

# get names of all 66 classes
CLASS_LIST = []
with open('all_heptatonic_scale_classes.txt', 'r') as f:
    for line in f:
        CLASS_LIST.append(eval(line))


# alternative names
ALTERNATIVE_NAME_SUBS = {
    'Ukrainian Dorian': 'Dorian(#4)',
    'Harmonic Minor': 'Aeolian(#7)',
    'Phrygian Dominant': 'Phrygian(#3)',
    'HMP5B': 'Phrygian(#3)',
    'Altered': 'Locrian(b4)',
    'Acoustic': 'Lydian(b7)',
    'Lydian Dominant': 'Lydian(b7)',
    'Melodic Minor': 'Dorian(#7)',
    'Minor Major': 'Ionian(b3)',
    'Melodic Major': 'Mixolydian(b6)',
    'Major Minor': 'Aeolian(#3)',
    'Half Diminished': 'Locrian(#2)',
    'Minor Neapolitan': 'Phrygian(#7)',
    'Harmonic Phrygian': 'Phrygian(#7)',
    'Harmonic Major': 'Ionian(b6)',
    'Harmonic Lydian': 'Lydian(b6)',
    'Hungarian Minor': 'Aeolian(#4, #7)',
    'Double Harmonic': 'Phrygian(#3, #7)',
    'Major Neapolitan': 'Phrygian(#6, #7)',
    'Melodic Phrygian': 'Phrygian(#6, #7)',
    'Major': 'Ionian',  # keep these two at the end!!!
    'Minor': 'Aeolian'  # keep these two at the end!!!
}


''' for Chord '''


CHORD_TYPE_TO_SCALE_TYPE = {
    'aug': 'Ionian(#5)',
    '': 'Ionian',
    '-5': 'Ionian(b5)',
    'm': 'Aeolian',
    'dim': 'Locrian',
    'dim-3': 'Locrian(b3)',
    'M7+5': 'Ionian(#5)',
    '7+5': 'Mixolydian(#5)',
    'M7': 'Ionian',
    '7': 'Mixolydian',
    '7-5': 'Mixolydian(b5)',
    'mM7': 'Aeolian(#7)',
    'm7': 'Aeolian',
    'm7-5': 'Locrian',
    'dim7': 'Locrian(b7)',
    'm7-5-3': 'Locrian(b3)',
    'dim7-3': 'Locrian(b7, b3)',  # b Dorian(#1)
    'sus2': 'Ionian',
    'sus4': 'Ionian',
    '6': 'Ionian',
    'm6': 'Dorian',
    '9': 'Mixolydian'
}

CHORD_TYPE_TO_STEPS = {
    'aug': [0, 2, 4],
    '': [0, 2, 4],
    '-5': [0, 2, 4],
    'm': [0, 2, 4],
    'dim': [0, 2, 4],
    'dim-3': [0, 2, 4],
    'M7+5': [0, 2, 4, 6],
    '7+5': [0, 2, 4, 6],
    'M7': [0, 2, 4, 6],
    '7': [0, 2, 4, 6],
    '7-5': [0, 2, 4, 6],
    'mM7': [0, 2, 4, 6],
    'm7': [0, 2, 4, 6],
    'm7-5': [0, 2, 4, 6],
    'dim7': [0, 2, 4, 6],
    'm7-5-3': [0, 2, 4, 6],
    'dim7-3': [0, 2, 4, 6],
    'sus2': [0, 1, 4],
    'sus4': [0, 3, 4],
    '6': [0, 2, 4, 5],
    'm6': [0, 2, 4, 5],
    '9': [0, 2, 4, 6, 1]
}

TENSION_NAME_TO_INTERVAL_NAME = {
    'b9': 'm9',
    '9': 'M9',
    '#9': 'A9',
    'b11': 'd11',
    '11': 'P11',
    '#11': 'A11',
    'b13': 'm13',
    '13': 'M13',
    '#13': 'A13'
}

INTERVAL_NAME_TO_TENSION_NAME = {
    'm9': 'b9',
    'M9': '9',
    'A9': '#9',
    'd11': 'b11',
    'P11': '11',
    'A11': '#11',
    'm13': 'b13',
    'M13': '13',
    'A13': '#13'
}

# recognize chord type from intervals
INTERVAL_VECTOR_TO_CHORD_TYPE = {
    '44': 'aug',
    '43': '',
    '42': '-5',
    '34': 'm',
    '33': 'dim',
    '24': 'dim-3',
    '443': 'M7+5',
    '442': '7+5',
    '434': 'M7',
    '433': '7',
    '424': '7-5',
    '344': 'mM7',
    '343': 'm7',
    '334': 'm7-5',
    '333': 'dim7',
    '244': 'm7-5-3',
    '243': 'dim7-3',
    '25': 'sus2',
    '52': 'sus4',
    '432': '6',  # dim7+5
    '342': 'm6',
    '4334': '9'
}

CHORD_TYPE_TO_COLOR = {
    'M7': 'red',
    'M7+5': 'magenta',
    '7': 'white',
    'mM7': 'cyan',
    'm7': 'blue',
    'm7-5': 'cyan',
    'dim7': 'green'
}
