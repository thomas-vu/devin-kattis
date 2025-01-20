def find_cd_singles(test_cases):
    results = []
    for case in test_cases:
        n = case[0]
        single_positions = case[1]
        download_positions = list(range(1, n + 1))
        
        single_top_n = case[1]
        download_top_n = list(range(1, n + 1))
        
        # Create a dictionary to count the occurrences of each position in the Download Top N
        download_count = {pos: 0 for pos in range(1, n + 1)}
        for pos in single_top_n:
            download_count[pos] += 1
        
        # Determine the singles that are certainly available as CD single
        cd_singles = []
        for i in range(n):
            if download_count[download_positions[i]] == 1:
                cd_singles.append(download_positions[i])
        
        results.append((len(cd_singles), cd_singles))
    
    return results

# Read input
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    single_positions = [int(input()) for _ in range(N)]
    test_cases.append((N, single_positions))

# Process and output the results
results = find_cd_singles(test_cases)
for result in results:
    print(result[0])
    for pos in sorted(result[1]):
        print(pos)