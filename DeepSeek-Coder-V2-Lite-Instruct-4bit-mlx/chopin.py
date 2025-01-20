key_names = {
    "Ab": "G# minor",
    "A#": "Bb major",
    "Cb": "B# minor",
    "Db": "C# major",
    "D#": "Eb minor",
    "Eb": "D# major",
    "Fb": "E# minor",
    "Gb": "F# major",
    "G#": "A# minor",
    "Abb": "Cb major",
    "Bb": "A# minor",
    "C#": "Db major",
    "D#b": "Eb minor",
    "E#b": "F# major",
    "F#": "Gb minor",
    "G#b": "A# major",
    "A#b": "Bb minor"
}

def find_alternate_key(note, tonality):
    key = f"{note} {tonality}"
    if key in key_names:
        return key_names[key]
    else:
        for alt_note, alt_key in key_names.items():
            if note == alt_note[:-1] and tonality != alt_key.split()[1]:
                return f"Case {case_number}: {alt_key}"
        return "UNIQUE"

import sys
case_number = 0
for line in sys.stdin:
    if not line.strip():
        continue
    case_number += 1
    note, tonality = line.strip().split()
    result = find_alternate_key(note, tonality)
    print(f"Case {case_number}: {result}")