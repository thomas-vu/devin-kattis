import sys

# Read input
n1, c1, s1, f1 = map(int, sys.stdin.readline().split())
alphabet1 = sys.stdin.readline().strip()
final_states1 = set(map(int, sys.stdin.readline().split()))
transition_table1 = [list(map(int, sys.stdin.readline().split())) for _ in range(n1)]

n2, c2, s2, f2 = map(int, sys.stdin.readline().split())
alphabet2 = sys.stdin.readline().strip()
final_states2 = set(map(int, sys.stdin.readline().split()))
transition_table2 = [list(map(int, sys.stdin.readline().split())) for _ in range(n2)]

# Initialize the new automaton
new_states = n1 * n2
new_initial_state = (s1 - 1) * n2 + (s2 - 1) + 1
new_final_states = set()
new_transition_table = [[0] * new_states for _ in range(new_states)]

# Compute the transition table of the new automaton
for i in range(new_states):
    for j in range(new_states):
        if i // n2 == j // n2:  # Same automaton part
            for a in range(c1):
                new_transition_table[i][j] |= (transition_table1[(i % n2)][a] << a) | (transition_table2[(j % n2)][a] << (c1 + a))
        else:  # Different automaton parts
            for a in range(c1):
                new_transition_table[i][j] |= (transition_table1[(i % n2)][a] << a) | (transition_table2[(j % n2)][a] << (c1 + a))

# Determine the final states of the new automaton
for i in range(new_states):
    if (i % n2 + 1) in final_states1 and (i // n2 + 1) in final_states2:
        new_final_states.add(i + 1)

# Output the new automaton
print(new_states, c1 + c2, new_initial_state, len(new_final_states))
print(alphabet1 + alphabet2)
for fs in new_final_states:
    print(fs, end=' ')
print()
for i in range(new_states):
    for j in range(new_states):
        print(' '.join(map(str, new_transition_table[i][j].to_bytes(new_states // n2, 'big'))), end=' ')
    print()