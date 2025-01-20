def decode_segments(display):
    segments = [['.' for _ in range(21)] for _ in range(7)]
    for i in range(7):
        for j in range(21):
            if display[i][j] == 'X':
                segments[i][j] = '1'
            elif display[i][j] == '.':
                segments[i][j] = '0'
            else:
                raise ValueError("Invalid character in display")
    return segments

def check_segments(segments):
    working = set()
    for segment in range(7):
        if all(segments[seg][segment] == '1' for seg in range(7)):
            working.add(segment)
    return working

def display_segments(segments):
    for i in range(7):
        print(''.join(segments[i]))

def main():
    n = int(input())
    displays = [input().strip() for _ in range(8 * n - 1)]
    
    decoded_displays = [decode_segments(displays[i * 8:(i + 1) * 8]) for i in range(n)]
    possible_segments = [set(range(7)) for _ in range(21)]
    
    for display in decoded_displays:
        for i in range(7):
            for j in range(21):
                if display[i][j] == '0' or display[i][j] == '1':
                    possible_segments[j].discard(i)
    
    for i in range(21):
        if len(possible_segments[i]) == 0:
            print("impossible")
            return
    
    final_segments = [['?' for _ in range(21)] for _ in range(7)]
    
    for i in range(7):
        for j in range(21):
            if len(possible_segments[j]) == 1:
                final_segments[int(list(possible_segments[j])[0])][j] = '1'
            else:
                final_segments[i][j] = display[i][j]
    
    for i in range(7):
        if '1' not in final_segments[i]:
            for j in range(21):
                if display[i][j] == '0':
                    final_segments[i][j] = '0'
    
    display_segments(final_segments)

if __name__ == "__main__":
    main()