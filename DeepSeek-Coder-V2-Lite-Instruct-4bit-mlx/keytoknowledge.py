def find_correct_answers(n, m, answers):
    from itertools import product
    
    # Generate all possible combinations of correct answers
    for combo in product([0, 1], repeat=m):
        count = sum(a == c for a, c in zip(combo, answers))
        if count == n:
            return ''.join(map(str, combo))
    return "0 solutions"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    test_cases = int(data[index])
    index += 1
    results = []
    
    for _ in range(test_cases):
        n, m = map(int, data[index].split())
        index += 1
        answers = []
        for i in range(n):
            answers.append(list(map(int, data[index].split()[0])))
            index += 1
        for i in range(n):
            c = int(data[index].split()[1])
            index += 1
            result = find_correct_answers(n, m, answers[i])
            results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()