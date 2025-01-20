def RATS(n):
    reversed_n = int(str(n)[::-1])
    sum_digits = n + reversed_n
    sorted_sum = int(''.join(sorted(str(sum_digits))))
    return sorted_sum

def process_sequence(initial_value, M):
    sequence = [initial_value]
    seen = set()
    
    for i in range(1, M):
        next_value = RATS(sequence[-1])
        if next_value in seen:
            return f"{initial_value} R {i}"
        if next_value in sequence:
            return f"{initial_value} C {sequence.index(next_value) + 1}"
        sequence.append(next_value)
        seen.add(next_value)
    
    return f"{initial_value} {sequence[-1]}"

def main():
    P = int(input())
    for _ in range(P):
        data_set_number, M, initial_value = input().split()
        M = int(M)
        result = process_sequence(int(initial_value), M)
        print(result)

if __name__ == "__main__":
    main()