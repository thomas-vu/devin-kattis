def count_imported_turtles(sequence):
    import_count = 0
    previous = sequence[0]
    
    for i in range(1, len(sequence) - 1):
        if sequence[i] > previous * 2:
            import_count += sequence[i] - previous * 2
        previous = sequence[i]
    
    return import_count

def main():
    T = int(input())
    for _ in range(T):
        sequence = list(map(int, input().split()))
        print(count_imported_turtles(sequence))

if __name__ == "__main__":
    main()