def is_language_empty(n, c, s, f, alphabet, final_states, transitions):
    # Create a graph representation of the automaton
    from collections import deque
    
    # Check if there is a path from the initial state to any final state
    visited = [False] * (n + 1)
    queue = deque([s])
    visited[s] = True
    
    while queue:
        state = queue.popleft()
        for symbol in range(1, c + 1):
            next_state = transitions[state][symbol - 1]
            if not visited[next_state]:
                visited[next_state] = True
                queue.append(next_state)
    
    # Check if any final state is reachable from the initial state
    for final_state in final_states:
        if visited[final_state]:
            return "non-empty"
    
    return "empty"

# Read input
n, c, s, f = map(int, input().split())
alphabet = input()
final_states = list(map(int, input().split()))
transitions = [list(map(int, input().split())) for _ in range(n)]

# Check if the language is empty and output the result
result = is_language_empty(n, c, s, f, alphabet, final_states, transitions)
print(result)