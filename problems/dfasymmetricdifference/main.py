def read_automaton():
    n = int(input())
    c = int(input())
    s = int(input())
    f = int(input())
    Sigma = input().strip()
    final_states = set(map(int, input().split()))
    transitions = [list(map(int, input().split())) for _ in range(n)]
    return n, c, s, f, Sigma, final_states, transitions

def build_symmetric_difference(A, B):
    n1, c1, s1, f1, Sigma1, final_states1, transitions1 = A
    n2, c2, s2, f2, Sigma2, final_states2, transitions2 = B
    
    # Create a new set of states for the symmetric difference automaton
    n = n1 * n2
    Sigma = Sigma1  # The alphabet remains the same
    
    # Determine new final states and transitions for the symmetric difference
    new_final_states = set()
    new_transitions = [[0] * n for _ in range(n)]
    
    # Helper function to get the state from A and B based on index
    def get_state(i, j):
        return i * n2 + j
    
    # Build the new transitions for the symmetric difference automaton
    for i in range(n1):
        for j in range(n2):
            state = get_state(i, j)
            for a in range(c):
                next_state_A = transitions1[i][a] - 1
                next_state_B = transitions2[j][a] - 1
                if next_state_A < 0 or next_state_B < 0:
                    new_transitions[state][a] = get_state(next_state_A, next_state_B)
                else:
                    new_transitions[state][a] = get_state(next_state_A, next_state_B)
    
    # Determine new final states for the symmetric difference automaton
    for i in range(n1):
        for j in range(n2):
            if (i + 1) in final_states1 and (j + 1) not in final_states2:
                new_final_states.add(get_state(i, j))
            elif (i + 1) not in final_states1 and (j + 1) in final_states2:
                new_final_states.add(get_state(i, j))
    
    return n, c, s1 * n2 + s2 - 1, len(new_final_states), Sigma, new_final_states, new_transitions

# Read the first automaton
A = read_automaton()

# Read the second automaton
B = read_automaton()

# Build the symmetric difference automaton
C = build_symmetric_difference(A, B)

# Output the symmetric difference automaton
n, c, s, f, Sigma, final_states, transitions = C
print(n)
print(c)
print(s + 1)
print(f)
print(Sigma)
for fs in final_states:
    print(fs, end=' ')
print()
for row in transitions:
    for val in row:
        print(val + 1, end=' ')
    print()