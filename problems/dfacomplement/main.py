n, c, s, f = map(int, input().split())
alphabet = input().strip()
final_states = set(map(int, input().split()))
transitions = [list(map(int, input().split())) for _ in range(n)]

# Create the complement automaton
new_transitions = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(c):
        new_transitions[i][j] = transitions[i][j]

# Determine the new final states
new_final_states = set(range(1, n+1)) - final_states

# Output the complement automaton
print(n, c, s, len(new_final_states))
print(''.join(alphabet))
for state in new_final_states:
    print(state, end=' ')
print()
for i in range(n):
    for j in range(c):
        print(new_transitions[i][j], end=' ')
    print()