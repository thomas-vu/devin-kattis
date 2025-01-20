def is_evenly_spaced(line):
    black_positions = [i for i, pixel in enumerate(line) if pixel == '*']
    if len(black_positions) <= 1:
        return "EVEN"
    spacing = black_positions[1] - black_positions[0]
    for i in range(2, len(black_positions)):
        if black_positions[i] - black_positions[i-1] != spacing:
            return "NOT EVEN"
    return "EVEN"

line_number = 1
while True:
    line = input()
    if line == "END":
        break
    print(f"{line_number} {is_evenly_spaced(line)}")
    line_number += 1