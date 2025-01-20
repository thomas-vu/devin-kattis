def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    Q = int(data[1])
    
    names = []
    for i in range(N):
        name1 = data[2*i + 2]
        name2 = data[2*i + 3]
        names.append((name1, name2))
    
    instructions = data[-Q]
    
    line = list(range(N))  # Each person's position in the queue
    yelled_names = set()
    
    for instruction in instructions:
        if instruction == 'F':
            line = [line[i] for i in range(len(line)) if i != 0] + [0]
        elif instruction == 'B':
            line = [line[-1]] + [line[i] for i in range(len(line) - 1)]
        elif instruction == 'R':
            if len(line) > 1:
                line = [line[i] for i in range(len(line)) if i != len(line) - 1] + [line[-1]]
            else:
                line = [0]
        elif instruction == 'C':
            if len(line) > 1:
                partner_idx = line.index([x for x in names if x[0] == names[line[-1]][1] or x[1] == names[line[-1]][1]][0])
                line = [line[i] for i in range(len(line)) if i != len(line) - 1] + [partner_idx]
        elif instruction == 'P':
            partner = names[line[-1]]
            if line[-1] == 0:
                yelled_names.add(partner[0])
            else:
                yelled_names.add(partner[1])
    
    for name in sorted(yelled_names):
        print(name)
    print()
    
    for person in line:
        print(names[person][0] if person == 0 else names[person][1])

main()