def main():
    n1, c, s1, f1 = map(int, input().split())
    Sigma1 = input()
    final_states1 = set(map(int, input().split()))
    transitions1 = [list(map(int, input().split())) for _ in range(n1)]

    n2, _, s2, f2 = map(int, input().split())
    Sigma2 = input()
    final_states2 = set(map(int, input().split()))
    transitions2 = [list(map(int, input().split())) for _ in range(n2)]

    n = n1 * n2
    new_transitions = [[0] * (c + 1) for _ in range(n + 1)]
    new_final_states = set()

    for i in range(1, n + 1):
        state = (i - 1) // n2
        q_state = i % n2 if i % n2 != 0 else n2
        for j in range(1, c + 1):
            new_transitions[i][j] = transitions2[q_state - 1][j - 1]
        if i % n2 == 0:
            new_transitions[i][c] = s2
        else:
            new_transitions[i][c] = transitions1[(i - 1) // n2][j - 1]

    for i in range(1, n + 1):
        if i % n2 == 0:
            for j in range(1, c + 1):
                if transitions2[n2 - 1][j - 1] not in final_states2 and (i // n2 + 1) not in final_states1:
                    new_final_states.add(i)
        else:
            if (i // n2 + 1) not in final_states1:
                new_final_states.add(i)

    print(n, c + 1, s1 * n2 + s2 - n2, len(new_final_states))
    print(''.join([Sigma1[j - 1] for j in range(1, c + 1)]) + ' ')
    print(' '.join(map(str, sorted(new_final_states))))
    for i in range(1, n + 1):
        print(' '.join(map(str, new_transitions[i])))

if __name__ == "__main__":
    main()