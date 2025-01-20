def count_wins(battles):
    wins = 0
    for battle in battles:
        if 'CD' not in battle and 'D' in battle:
            wins += 1
    return wins

n = int(input())
battles = [input() for _ in range(n)]
print(count_wins(battles))