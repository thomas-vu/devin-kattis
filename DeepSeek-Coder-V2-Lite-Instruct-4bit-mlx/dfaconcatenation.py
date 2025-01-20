def main():
    # Read the first automaton
    n1, c1, s1, f1 = map(int, input().split())
    sigma1 = input()
    final_states1 = list(map(int, input().split()))
    transitions1 = [list(map(int, input().split())) for _ in range(n1)]

    # Read the second automaton
    n2, c2, s2, f2 = map(int, input().split())
    sigma2 = input()
    final_states2 = list(map(int, input().split()))
    transitions2 = [list(map(int, input().split())) for _ in range(n2)]

    # Create the new states and transitions for the concatenation
    n = n1 * n2
    c = c1
    s = (s1 - 1) * n2 + (s2 - 1) + 1
    final_states = [(state - 1) * n2 + final_state for state in final_states1 for final_state in final_states2]
    transitions = []

    # Build the new transitions table
    for i in range(n1):
        for j in range(n2):
            for k in range(c):
                transitions.append(((i * n2 + j) - 1) * n2 + (transitions1[i][k] - 1) * n2 + transitions2[j][k])

    # Output the new automaton
    print(n)
    print(c, end=' ')
    for sym in sigma2:
        print(sym, end=' ')
    print()
    print(len([x for x in final_states if x <= n * n2]))
    for fs in final_states:
        print(fs, end=' ')
    print()
    for i in range(n):
        for j in range(c):
            print((i // n2) * n2 + transitions[i * c + j], end=' ')
        print()

if __name__ == "__main__":
    main()