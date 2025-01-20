def min_steps_to_sort_books(stack):
    steps = 0
    while not is_sorted(stack):
        for i in range(len(stack) - 1):
            if stack[i] > stack[i + 1]:
                stack = stack[:i] + stack[i + 1:] + stack[i:i + 2]
                steps += 1
                break
    return steps

def is_sorted(stack):
    for i in range(len(stack) - 1):
        if stack[i] > stack[i + 1]:
            return False
    return True

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    num_test_cases = int(data[index])
    index += 1
    results = []
    
    for _ in range(num_test_cases):
        n = int(data[index])
        index += 1
        stack = list(map(int, data[index].split()))
        index += 1
        results.append(min_steps_to_sort_books(stack))
    
    for result in results:
        print(result)

main()