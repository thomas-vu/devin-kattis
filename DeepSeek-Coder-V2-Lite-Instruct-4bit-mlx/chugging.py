def chugging_time(N, tA, dA, tB, dB):
    alice_total = sum([tA + i * dA for i in range(N)])
    bob_total = sum([tB + i * dB for i in range(N)])
    if alice_total < bob_total:
        return "Alice"
    elif alice_total > bob_total:
        return "Bob"
    else:
        return "="

# Read input
N = int(input())
tA, dA = map(int, input().split())
tB, dB = map(int, input().split())

# Output the result
print(chugging_time(N, tA, dA, tB, dB))