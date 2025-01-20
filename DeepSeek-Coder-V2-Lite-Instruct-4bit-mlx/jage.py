def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    
    students = data[2:N+2]
    tags = [data[N+2 + i].split() for i in range(M)]
    
    tag_graph = {student: [] for student in students}
    for t in tags:
        tag_graph[t[0]].append(t[1])
    
    hunters = set([students[0]])
    cheats = set()
    
    for tag in tags:
        if tag[1] not in hunters:
            cheats.add(tag[0])
        else:
            hunters.remove(tag[1])
            hunters.add(tag[0])
    
    cheaters = sorted(list(cheats))
    print(len(cheaters))
    if len(cheaters) > 0:
        print('\n'.join(cheaters))

if __name__ == "__main__":
    main()