N, M = map(int, input().split())
S = input()
T = input()

def translate_line(L, S, T):
    translation = str.maketrans(S, T)
    L_translated = L.translate(translation)
    return compress_line(L_translated)

def compress_line(L):
    compressed = ""
    i = 0
    while i < len(L):
        count = 1
        while i + count < len(L) and L[i] == ' ' and L[i+count] == ' ':
            count += 1
        if count >= 4:
            compressed += '&' + format(count, '02d')
        else:
            compressed += L[i] * count
        i += count
    return compressed

def concatenate_lines(lines, N):
    result = []
    current_line = ""
    for line in lines:
        if len(current_line) + len(line) <= N:
            current_line += line
        else:
            result.append(current_line)
            current_line = line
    if current_line:
        result.append(current_line)
    return result

lines = []
while True:
    line = input()
    if line == '****':
        break
    lines.append(line)

translated_lines = [translate_line(L, S, T) for L in lines]
concatenated_lines = concatenate_lines(translated_lines, N)
for line in concatenated_lines:
    print(line)