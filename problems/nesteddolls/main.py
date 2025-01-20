def min_nested_dolls(test_cases):
    results = []
    for case in test_cases:
        m = case[0]
        dolls = [(case[i], case[i+1]) for i in range(1, len(case), 2)]
        dolls.sort(key=lambda x: (x[0], -x[1]))
        stack = []
        for doll in dolls:
            if not stack or stack[-1] < (doll[0], doll[1]):
                stack.append(doll)
            else:
                idx = len(stack) - 1
                while idx >= 0 and stack[idx] > (doll[0], doll[1]):
                    idx -= 1
                stack[idx + 1] = (doll[0], doll[1])
        results.append(len(stack))
    return results

# Read input
t = int(input().strip())
test_cases = []
for _ in range(t):
    m = int(input().strip())
    case = list(map(int, input().split()))
    test_cases.append(case)

# Process and output results
results = min_nested_dolls(test_cases)
for result in results:
    print(result)