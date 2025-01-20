def who_wins(s):
    n = len(s)
    if n % 2 == 0:
        return "Chikapu"
    else:
        if s[0] == s[-1]:
            return "Chikapu"
        else:
            return "Bash"

# Read the number of test cases
T = int(input())
for _ in range(T):
    S = input().strip()
    winner = who_wins(S)
    print(winner)