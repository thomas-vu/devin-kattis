def generate_scale(root):
    scale = [root]
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    intervals = [0, 2, 4, 5, 7, 9, 11]
    for interval in intervals:
        next_note = (scale[-1] + interval) % 12
        scale.append(notes[next_note])
    return set(scale)

def find_scales(song):
    all_scales = []
    for root in ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']:
        scale = generate_scale(root)
        if all(note in scale for note in song):
            all_scales.append(root)
    return all_scales

n = int(input().strip())
song = input().strip().split()
scales = find_scales(song)
if scales:
    print(' '.join(sorted(scales)))
else:
    print('none')