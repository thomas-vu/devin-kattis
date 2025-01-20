def can_distribute_candies(test_cases):
    results = []
    for case in test_cases:
        candies = [int(input()) for _ in range(int(input()))]
        total_candies = sum(candies)
        if total_candies % len(candies) == 0:
            results.append("YES")
        else:
            results.append("NO")
    return results

T = int(input())
test_cases = [None] * T
for i in range(T):
    input()  # consume the blank line
    test_cases[i] = [input().strip() for _ in range(int(input()))]

results = can_distribute_candies(test_cases)
for result in results:
    print(result)