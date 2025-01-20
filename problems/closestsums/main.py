def closest_sum(numbers, query):
    numbers = sorted(numbers)
    closest_sums = []
    
    for q in query:
        min_diff = float('inf')
        closest_sum = None
        
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                current_sum = numbers[i] + numbers[j]
                diff = abs(current_sum - q)
                
                if diff < min_diff:
                    min_diff = diff
                    closest_sum = current_sum
                elif diff == min_diff and current_sum < closest_sum:
                    closest_sum = current_sum
        
        closest_sums.append(f"Closest sum to {q} is {closest_sum}.")
    
    return closest_sums

def main():
    case = 1
    while True:
        try:
            n = int(input())
            numbers = [int(input()) for _ in range(n)]
            m = int(input())
            queries = [int(input()) for _ in range(m)]
            
            results = closest_sum(numbers, queries)
            
            print(f"Case {case}:")
            for result in results:
                print(result)
            
            case += 1
        except EOFError:
            break

if __name__ == "__main__":
    main()