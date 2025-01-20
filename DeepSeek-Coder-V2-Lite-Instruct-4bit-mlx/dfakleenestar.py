# Read input
n, c, s, f = map(int, input().split())
alphabet = input().strip()
final_states = set(map(int, input().split()))
transitions = [list(map(int, input().split())) for _ in range(n)]

# Create the epsilon closure function
def epsilon_closure(state, transitions):
    stack = [state]
    closure = set()
    while stack:
        state = stack.pop()
        if state not in closure:
            closure.add(state)
            stack.extend(transitions[state - 1][:c])
    return closure

# Create the new states and transitions for the Kleene star
new_states = set()
new_transitions = []
new_final_states = set()

# Add new start state and its epsilon closure
new_start_state = n * c + 1
new_states.add(new_start_state)
epsilon_closure_start = epsilon_closure(s, transitions)
for state in epsilon_closure_start:
    new_states.add(state)
new_transitions.extend([0] * (c * n))

# Add new states and transitions for each state in the original automaton
for i in range(1, n + 1):
    for j in range(1, c + 1):
        new_state = n * (j - 1) + i
        new_states.add(new_state)
        new_transitions.extend([0] * (c * n))
        if i in final_states:
            new_final_states.add(new_state)
        for k in range(1, n + 1):
            new_transitions[new_state - 1 + (k - 1) * n] = transitions[i - 1][j - 1]

# Add new final states and epsilon transitions to the original accepting states
for state in new_final_states:
    for final_state in epsilon_closure(s, transitions):
        new_final_states.add(final_state)
    for k in range(1, n + 1):
        new_transitions[state - 1 + (k - 1) * n] = k

# Output the new automaton
print(len(new_states), c, 1, len(new_final_states))
print(''.join(alphabet))
for final_state in new_final_states:
    print(final_state, end=' ')
print()
for i in range(1, n + 1):
    for j in range(1, c + 1):
        print(new_transitions[(i - 1) * n + (j - 1)], end=' ')
    print()