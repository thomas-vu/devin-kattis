def is_non_boring(sequence):
    last_seen = {}
    for i, num in enumerate(sequence):
        if num in last_seen:
            return "boring"
        last_seen[num] = i
    return "non-boring"

def main():
    T = int(input())
    results = []
    for _ in range(T):
        n = int(input())
        sequence = list(map(int, input().split()))
        results.append(is_non_boring(sequence))
    for result in results:
        print(result)

main()