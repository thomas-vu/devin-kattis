def can_install(L, x, y):
    total_cost = 0
    for length in L:
        total_cost += (length * x)
    average_cost = total_cost / len(L)
    return average_cost <= y

def main():
    N = int(input())
    x = int(input())
    y = int(input())
    L = list(map(int, input().split()))
    
    left = 0
    right = N
    
    while left < right:
        mid = (left + right + 1) // 2
        selected_locations = L[:mid]
        if can_install(selected_locations, x, y):
            left = mid
        else:
            right = mid - 1
    
    print(left)

if __name__ == "__main__":
    main()