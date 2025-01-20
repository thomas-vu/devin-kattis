def min_digit_changes(numbers):
    n, m = map(int, input().split())
    numbers = [input().zfill(m) for _ in range(n)]
    
    numbers.sort()
    changes = [0] * n
    
    for i in range(1, n):
        diff = 0
        for j in range(m):
            if numbers[i][j] != numbers[i-1][j]:
                diff += 1
        changes[i] = diff
    
    min_changes = sum(changes)
    print('\n'.join(numbers))
    
min_digit_changes([])