def note_to_index(note):
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    return notes.index(note)

def index_to_note(index):
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    return notes[index]

def find_relation(melody1, melody2):
    l = len(melody1)
    if melody2 == melody1:
        return "Nonsense"
    
    # Check for transposition
    shift = (note_to_index(melody2[0]) - note_to_index(melody1[0])) % 12
    transposed = [index_to_note((note_to_index(melody1[i]) + shift) % 12) for i in range(l)]
    if melody2 == transposed:
        return "Transposition"
    
    # Check for retrograde
    reversed_melody2 = melody2[::-1]
    if melody2 == reversed_melody2:
        return "Retrograde"
    
    # Check for inversion
    inverted = [melody1[0]] + [index_to_note((-note_to_index(melody1[i]) + 2 * note_to_index(melody1[0])) % 12) for i in range(1, l)]
    if melody2 == inverted:
        return "Inversion"
    
    return "Nonsense"

# Read input
l = int(input())
melody1 = input().split()
melody2 = input().split()

# Determine the relation and output the result
print(find_relation(melody1, melody2))