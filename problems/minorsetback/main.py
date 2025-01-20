import sys

# Helper function to convert frequency to pitch name
def freq_to_pitch(freq):
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    base_freq = 440.0
    for i in range(12):
        if abs(freq - base_freq * (2 ** (i / 12))) < 1e-4:
            return notes[i % 12] + ("#" if i % 12 in [0, 3, 5, 7, 8, 10] else "")
    return None

# Helper function to determine the key from allowed pitches
def determine_key(allowed_pitches):
    keys = {
        "G major": ["G", "A", "B", "C", "D", "E", "F#"],
        "F# minor": ["F#", "G#", "A", "B", "C#", "D", "E"],
        "C major": ["C", "D", "E", "F", "G", "A", "B"],
        "G minor": ["G", "A", "Bb", "C", "D", "Eb", "F#"],
        "Eb major": ["Eb", "F", "G", "Ab", "Bb", "C", "D"],
        "A minor": ["A", "B", "Cb", "C#", "D#", "Eb", "Gb"]
    }
    
    for key, pitches in keys.items():
        if all(pitch in allowed_pitches for pitch in pitches):
            return key
    return None

# Read input
N = int(sys.stdin.readline().strip())
frequencies = [float(sys.stdin.readline().strip()) for _ in range(N)]

# Determine the key using allowed pitches from each frequency's pitch name
allowed_pitches = set()
for freq in frequencies:
    pitch = freq_to_pitch(freq)
    if pitch is not None:
        allowed_pitches.add(pitch)

key = determine_key(allowed_pitches)
if key is None:
    print("cannot determine key")
else:
    # Translate the song into pitch names in the determined key
    for freq in frequencies:
        print(freq_to_pitch(freq))