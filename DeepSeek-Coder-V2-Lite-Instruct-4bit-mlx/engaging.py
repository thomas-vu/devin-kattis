def main():
    m, n, k = map(int, input().split())
    survey_data = [list(map(int, input().split())) for _ in range(k)]
    
    # Create a dictionary to store the satisfaction levels for each customer
    satisfaction_levels = {customer: [] for customer in range(1, n + 1)}
    
    # Populate the dictionary with survey data
    for i, j, p in survey_data:
        if p != 0:
            satisfaction_levels[i].append((j, p))
    
    # Initialize the best sum of satisfaction and the list of gifts to send
    best_sum = 0
    gift_allocation = []
    
    # Try all possible combinations of gifts to send to customers
    from itertools import permutations
    
    for perm in permutations(range(1, m + 1), n):
        current_sum = 0
        temp_allocation = []
        
        for customer, gift in zip(range(1, n + 1), perm):
            if satisfaction_levels[customer]:
                for g, s in satisfaction_levels[customer]:
                    if g == gift:
                        current_sum += s
                        temp_allocation.append((customer, gift))
        
        if current_sum > best_sum:
            best_sum = current_sum
            gift_allocation = temp_allocation
    
    # Output the results
    print(best_sum)
    print(len(gift_allocation))
    for x, y in gift_allocation:
        print(x, y)

if __name__ == "__main__":
    main()