def parse_input():
    n = int(input())
    notes = input().split()
    return n, notes

def generate_staff(notes):
    staff = {
        'G': ['', '', '', '', '', '', '', '', '', '', '', '', ''],
        'F': ['', '', '', '', '', '', '', '', '', '', '', '', ''],
        'E': ['', '', '', '', '', '', '', '', '', '', '', '', ''],
        'D': ['', '', '', '', '', '', '', '', '', '', '', '', ''],
        'C': ['', '', '', '', '', '', '', '', '', '', '', '', ''],
        'B': ['', '', '', '', '', '', '', '', '', '', '', '', ''],
        'A': ['', '', '', '', '', '', '', '', '', '', '', '', ''],
        'g': ['', '', '', '', '', '', '', '', '', '', '', '', ''],
        'f': ['', '', '', '', '', '', '', '', '', '', '', '', ''],
        'e': ['', '', '', '', '', '', '', '', '', '', '', '', ''],
        'd': ['', '', '', '', '', '', '', '', '', '', '', '', ''],
        'c': ['', '', '', '', '', '', '', '', '', '', '', '', ''],
        'b': ['', '', '', '', '', '', '', '', '', '', '', '', ''],
        'a': ['', '', '', '', '', '', '', '', '', '', '', '', '']
    }
    
    for note in notes:
        pitch = note[0]
        duration = int(note[1:]) if len(note) > 1 else 1
        line = staff[pitch]
        for i in range(duration):
            if len(line) > 0:
                line[i] = '*'
    
    return staff

def print_staff(staff):
    for key in sorted(staff.keys()):
        line = staff[key]
        print(f"{key}:", end='')
        for l in line:
            if not l:
                print("                                                            ", end='')
            else:
                print(l, end='')
        print()

def main():
    n, notes = parse_input()
    staff = generate_staff(notes)
    print_staff(staff)

if __name__ == "__main__":
    main()