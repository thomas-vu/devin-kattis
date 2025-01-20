def solve(N, M, translator_pairs):
    from collections import defaultdict

    language_speakers = defaultdict(set)
    for translator, languages in enumerate(translator_pairs):
        for language in languages:
            language_speakers[language].add(translator)

    paired = [False] * M
    pairings = []

    for i in range(M):
        if not paired[i]:
            for j in range(i + 1, M):
                if not paired[j] and translator_pairs[i][0] in language_speakers[translator_pairs[j][1]] and translator_pairs[i][1] in language_speakers[translator_pairs[j][0]]:
                    pairings.append((i, j))
                    paired[i] = True
                    paired[j] = True
                    break

    if all(paired):
        for pair in pairings:
            print(pair[0], pair[1])
    else:
        print("impossible")

# Read input
N, M = map(int, input().split())
translator_pairs = [list(map(int, input().split())) for _ in range(M)]
solve(N, M, translator_pairs)