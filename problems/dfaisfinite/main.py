def is_finite(n, c, s, f, alphabet, final_states, transitions):
    visited = set()
    
    def dfs(state):
        if state in final_states:
            return True
        if state in visited:
            return False
        visited.add(state)
        for symbol, next_state in enumerate(transitions[state]):
            if dfs(next_state):
                return True
        return False
    
    return dfs(s)

# Read input
n, c, s, f = map(int, input().split())
alphabet = input().split()
final_states = set(map(int, input().split()))
transitions = [list(map(int, input().split())) for _ in range(n)]

# Determine if the language is finite
if is_finite(n, c, s, f, alphabet, final_states, transitions):
    print("finite")
else:
    print("infinite")