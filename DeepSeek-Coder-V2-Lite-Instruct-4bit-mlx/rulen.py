def rule90(N, L, R, initial_states):
    def next_state(pattern):
        index = int(''.join(map(str, pattern[1:-1])), 2)
        return str((N >> index) & 1)
    
    states = list(initial_states)
    for _ in range(R):
        new_states = []
        for i in range(L):
            left = states[i - 1] if i > 0 else '0'
            center = states[i]
            right = states[(i + 1) % L] if i < L - 1 else '0'
            new_states.append(next_state([left, center, right]))
        states = new_states
    return states

# Read input
import sys
input = sys.stdin.read
data = input().split()
N, L, R = int(data[0]), int(data[1]), int(data[2])
initial_states = data[3]

# Compute and print the states for each iteration
for state in rule90(N, L, R, initial_states):
    print(state)