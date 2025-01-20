from collections import deque, defaultdict

def shortest_word_in_language(n, c, s, f, alphabet, final_states, transitions):
    queue = deque([(s, '')])  # (state, word)
    visited = set()
    while queue:
        state, word = queue.popleft()
        if state in final_states:
            return len(word)
        for symbol, next_state in zip(alphabet, transitions[state]):
            if (next_state, word + symbol) not in visited:
                visited.add((next_state, word + symbol))
                queue.append((next_state, word + symbol))
    return -1  # This should never be reached if the language is non-empty.

# Read input
n, c, s, f = map(int, input().split())
alphabet = input().split()
final_states = set(map(int, input().split()))
transitions = defaultdict(list)
for _ in range(n):
    transitions[_] = list(map(int, input().split()))

# Output the length of the shortest word in the language
print(shortest_word_in_language(n, c, s, f, alphabet, final_states, transitions))