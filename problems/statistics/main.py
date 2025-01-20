def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    case_number = 0
    n = int(data[case_number])
    while n != -1:
        case_number += 1
        numbers = list(map(int, data[case_number:case_number + n]))
        min_val = min(numbers)
        max_val = max(numbers)
        range_val = max_val - min_val
        print(f"Case {case_number}: {min_val} {max_val} {range_val}")
        case_number += n
        n = int(data[case_number]) if case_number < len(data) else -1

if __name__ == "__main__":
    main()