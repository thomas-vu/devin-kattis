def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n1 = int(data[0])
    c1 = int(data[1])
    s1 = int(data[2])
    f1 = int(data[3])
    alphabet = data[4]
    final_states1 = set(map(int, data[5:5+f1]))
    transitions1 = [list(map(int, data[6:][i*c1:(i+1)*c1])) for i in range(n1)]
    
    n2 = int(data[4+n1*c1])
    c2 = int(data[5+n1*c1])
    s2 = int(data[6+n1*c1])
    f2 = int(data[7+n1*c1])
    alphabet += data[8+n1*c1]
    final_states2 = set(map(int, data[9+n1*c1:]))
    transitions2 = [list(map(int, data[10+n1*c1:][i*c2:(i+1)*c2])) for i in range(n2)]
    
    n = n1 * n2
    c = len(alphabet)
    s = (s1 - 1) * n2 + (s2 - 1) * n2 + 1
    final_states = set()
    
    for fs1 in final_states1:
        for fs2 in final_states2:
            final_states.add((fs1 - 1) * n2 + (fs2 - 1) * n2 + 1)
    
    transitions = [[0] * c for _ in range(n)]
    
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            for k in range(c):
                transitions[(i - 1) * n2 + (j - 1)][k] = transitions1[(i - 1)][k] + (j - 1) * n2
    
    for i in range(1, n2 + 1):
        for j in range(c):
            for k in range(n1):
                transitions[(k + 1 - 1) * n2 + (i - 1)][j] = transitions2[(i - 1)][j] + (k) * n2
    
    print(n, c, s, len(final_states))
    print(alphabet)
    for fs in final_states:
        print(fs, end=' ')
    print()
    for i in range(n):
        for j in range(c):
            print(transitions[i][j], end=' ')
        print()

if __name__ == "__main__":
    main()