n = int(input())
contestants = {}
for _ in range(n):
    name, guess = input().split()
    contestants[int(guess)] = name
q = int(input())
ideas = [int(input()) for _ in range(q)]
for idea in ideas:
    closest_guess = min([g for g in contestants if g <= idea], default=None)
    winner_name = contestants[closest_guess] if closest_guess is not None else ':(',
    print(winner_name)