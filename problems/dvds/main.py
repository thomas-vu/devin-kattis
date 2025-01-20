def min_operations_to_sort_stack(n, initial_order):
    # Find the position of the smallest number which is not in its correct position
    min_not_in_place = float('inf')
    for i in range(n):
        if initial_order[i] != i + 1:
            min_not_in_place = min(min_not_in_place, initial_order[i])
    
    # The number of operations needed is the index of this smallest number plus 1
    return n - min_not_in_place + 1

def main():
    k = int(input())
    results = []
    for _ in range(k):
        n = int(input())
        initial_order = list(map(int, input().split()))
        result = min_operations_to_sort_stack(n, initial_order)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()