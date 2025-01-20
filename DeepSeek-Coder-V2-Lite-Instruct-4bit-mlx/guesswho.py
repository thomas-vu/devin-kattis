def find_hidden_character(characters, questions):
    possible_indices = set(range(len(characters)))
    
    for attr, resp in questions:
        new_possible_indices = set()
        for idx in possible_indices:
            if characters[idx][attr-1] == resp:
                new_possible_indices.add(idx)
        possible_indices = new_possible_indices
    
    if len(possible_indices) == 1:
        return "unique", list(possible_indices)[0] + 1
    else:
        return "ambiguous", len(possible_indices)

# Read input
N, M, Q = map(int, input().split())
characters = [input() for _ in range(N)]
questions = [tuple(input().split()) for _ in range(Q)]
for i in range(Q):
    questions[i] = (int(questions[i][0]), questions[i][1])

# Determine the hidden character
result, answer = find_hidden_character(characters, questions)
print(result)
if result == "unique":
    print(answer)
else:
    print(answer)