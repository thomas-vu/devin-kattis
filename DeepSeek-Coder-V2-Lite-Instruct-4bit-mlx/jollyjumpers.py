def is_jolly_jumper(sequence):
    n = sequence[0]
    if n == 1:
        return "Jolly"
    
    differences = set()
    for i in range(1, n):
        diff = abs(sequence[i] - sequence[i + 1])
        differences.add(diff)
    
    for i in range(1, n):
        if i not in differences:
            return "Not jolly"
    return "Jolly"

def main():
    while True:
        try:
            sequence = list(map(int, input().split()))
            result = is_jolly_jumper(sequence)
            print(result)
        except EOFError:
            break

if __name__ == "__main__":
    main()