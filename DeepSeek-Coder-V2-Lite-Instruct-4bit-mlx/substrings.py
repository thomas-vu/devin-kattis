def count_repeated_substrings(s):
    n = len(s)
    substrings = set()
    count = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            substring = s[i:j+1]
            if substring in substrings and substring not in repeated_substrings:
                count += 1
                repeated_substrings.add(substring)
            substrings.add(substring)
    
    return count

num_cases = int(input())
for _ in range(num_cases):
    s = input().strip()
    repeated_substrings = set()
    result = count_repeated_substrings(s)
    print(result)