def distribute_cost(price, contributions):
    total_amount = sum(contributions)
    individual_share = price / n
    remainder = price % n
    
    # Sort contributions in descending order to prioritize higher amounts
    sorted_contributions = sorted(contributions, reverse=True)
    
    # Distribute the cost as fairly as possible
    distribution = [int(individual_share) for _ in range(n)]
    
    # Distribute the remainder to some people if possible
    for i in range(remainder):
        distribution[i] += 1
    
    # Sort the distribution in ascending order of original contributions
    original_order = sorted(range(n), key=lambda x: contributions[x])
    distribution_sorted = [distribution[i] for i in original_order]
    
    return distribution_sorted

def main():
    test_cases = int(input())
    
    for _ in range(test_cases):
        price, n = map(int, input().split())
        contributions = list(map(int, input().split()))
        
        if sum(contributions) < price:
            print("IMPOSSIBLE")
        else:
            distribution = distribute_cost(price, contributions)
            print(' '.join(map(str, distribution)))

if __name__ == "__main__":
    main()