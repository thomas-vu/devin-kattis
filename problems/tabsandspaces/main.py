def find_tab_width(file):
    lines = file.split('\n')
    tab_widths = []
    
    for i in range(1, int(lines[0]) + 1):
        line = lines[i]
        spaces = [j for j in range(len(line)) if line.startswith(' ' * (j + 1))]
        tab_widths.append(min([space - sum((line[x] == ' ') * (x // tab_width) for x in range(space)) for space in spaces]))
    
    min_tab_width = min([tw for tw in tab_widths if tab_widths.count(tw) == 1])
    total_saved = sum((line.count(' ') - line.count('\t') * min_tab_width) for line in lines[1:])
    
    return min_tab_width, total_saved

files = []
file_count = int(input())
for _ in range(file_count):
    file = ''
    line_count = int(input())
    for _ in range(line_count):
        file += input() + '\n'
    files.append(file)

for file in files:
    min_tab_width, total_saved = find_tab_width(file)
    print(min_tab_width)
    print(total_saved)