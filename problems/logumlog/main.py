def parse_note(note):
    base = note[:-1]
    octave = int(note[-1])
    if '#' in note:
        base += '#'
    elif 'b' in note:
        base += 'b'
    return (base, octave)

def get_note_frequency(note):
    note_frequencies = {
        'C': 261.63,
        'C#': 277.18,
        'D': 293.66,
        'D#': 311.13,
        'E': 329.63,
        'F': 349.23,
        'F#': 369.99,
        'G': 392.00,
        'G#': 415.30,
        'A': 440.00,
        'A#': 466.16,
        'Bb': 466.16,
        'B': 493.88,
        'Cb': 0,
        'Db': 554.37,
        'Eb': 587.33,
        'Fb': 554.37,
        'Gb': 622.25,
        'Ab': 659.25,
        'Bb': 698.46
    }
    return note_frequencies[note]

def transpose(note, semitones):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    index = notes.index(note)
    new_index = (index + semitones) % 12
    return notes[new_index] + str(int(note[-1]) + (semitones // 12))

def is_same(melody1, melody2):
    if len(melody1) != len(melody2):
        return False
    
    for i in range(len(melody1)):
        note1 = melody1[i]
        note2 = melody2[i]
        
        if note1 == '-' or note2 == '-':
            continue
        
        base1, octave1 = parse_note(note1)
        base2, octave2 = parse_note(note2)
        
        if base1 != base2:
            return False
        
        frequency1 = get_note_frequency(base1 + str(octave1))
        frequency2 = get_note_frequency(base2 + str(octave2))
        
        if frequency1 != frequency2:
            return False
    
    return True

# Read input
n = int(input())
melody1 = list(map(str, input().split()))
melody2 = list(map(str, input().split()))

# Check if melodies are the same
if is_same(melody1, melody2):
    print("Jebb")
else:
    print("Neibb")