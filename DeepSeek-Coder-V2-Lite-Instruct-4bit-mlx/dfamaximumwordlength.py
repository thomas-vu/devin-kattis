def longest_word_length(n, c, s, f, alphabet, final_states, transitions):
    from collections import deque
    
    # Initialize the queue with the start state and an empty word
    queue = deque([(s, 0)])
    visited = set()
    
    while queue:
        state, length = queue.popleft()
        
        # If the current state is a final state, return the length of the word found so far
        if state in final_states:
            return length
        
        # Mark the current state as visited to avoid revisiting
        visited.add(state)
        
        # Explore the transitions from the current state
        for symbol, next_state in enumerate(transitions[state]):
            if next_state not in visited:
                queue.append((next_state, length + 1))
    
    return -1

# Read input
n, c, s, f = map(int, input().split())
alphabet = input().strip()
final_states = set(map(int, input().split()))
transitions = [list(map(int, input().split())) for _ in range(n)]

# Get the length of the longest word accepted by the automaton
result = longest_word_length(n, c, s, f, alphabet, final_states, transitions)
print(result)