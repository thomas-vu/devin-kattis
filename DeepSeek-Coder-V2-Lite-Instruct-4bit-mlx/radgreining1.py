n, m = map(int, input().split())
dna_sequence = [''] * n
contradiction = False

for _ in range(m):
    s, section = input().split()
    s = int(s) - 1
    for i in range(len(section)):
        if dna_sequence[s + i] == '' or dna_sequence[s + i] == section[i]:
            dna_sequence[s + i] = section[i]
        elif dna_sequence[s + i] != section[i]:
            contradiction = True

if contradiction:
    print('Villa')
else:
    for i in range(n):
        if dna_sequence[i] == '':
            dna_sequence[i] = '?'
    print(''.join(dna_sequence))