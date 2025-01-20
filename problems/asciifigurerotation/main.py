def rotate_figure(figure):
    lines = figure.split('\n')[1:]
    rotated_lines = ['' for _ in range(len(lines[0]))]
    
    for line in lines:
        for i, char in enumerate(line):
            rotated_lines[i] += char
    
    return '\n'.join(rotated_lines)

figures = []
while True:
    n = int(input())
    if n == 0:
        break
    figure = ''
    for _ in range(n):
        figure += input() + '\n'
    figures.append(figure)

for figure in figures:
    rotated = rotate_figure(figure)
    print(rotated)
    if figures.index(figure) < len(figures) - 1:
        print()