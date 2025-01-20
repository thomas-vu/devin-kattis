def calculate_win_average(n, k, games):
    from collections import defaultdict
    
    wins = defaultdict(int)
    losses = defaultdict(int)
    
    for _ in range(k * n * (n - 1) // 2):
        p1, m1, p2, m2 = input().split()
        p1, p2 = int(p1), int(p2)
        
        if m1 == m2:
            continue
        elif (m1 == 'rock' and m2 == 'scissors') or (m1 == 'scissors' and m2 == 'paper') or (m1 == 'paper' and m2 == 'rock'):
            wins[p1] += 1
            losses[p2] += 1
        else:
            wins[p2] += 1
            losses[p1] += 1
    
    for i in range(1, n + 1):
        total_games = wins[i] + losses[i]
        if total_games == 0:
            print("0.000")
        else:
            win_average = wins[i] / total_games
            print("{:.3f}".format(win_average))
    print()

while True:
    n, k = map(int, input().split())
    if n == 0:
        break
    games = [input().split() for _ in range(k * n * (n - 1) // 2)]
    calculate_win_average(n, k, games)