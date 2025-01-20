def find_climbing_sequence(distances):
    n = len(distances)
    height = 0
    sequence = []
    
    for i in range(n):
        if height + distances[i] >= 0:
            sequence.append('U')
            height += distances[i]
        elif height - distances[i] >= 0:
            sequence.append('D')
            height -= distances[i]
        else:
            return "IMPOSSIBLE"
    
    if height != 0:
        return "IMPOSSIBLE"
    
    return ''.join(sequence)

def main():
    N = int(input())
    for _ in range(N):
        M = int(input())
        distances = list(map(int, input().split()))
        result = find_climbing_sequence(distances)
        print(result)

if __name__ == "__main__":
    main()