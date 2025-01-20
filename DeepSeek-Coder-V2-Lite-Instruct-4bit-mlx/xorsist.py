def find_possessed(N):
    if N % 4 == 0:
        return 'Enginn'
    elif N % 4 == 1:
        return 'Gunnar'
    else:
        return N + 1 - (N // 2) * 2

# Read the input
N = int(input())
result = find_possessed(N)
print(result)