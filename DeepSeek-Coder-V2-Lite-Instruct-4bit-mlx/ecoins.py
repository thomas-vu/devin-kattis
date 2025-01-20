import math
from collections import deque

def min_coins(S, coins):
    # Use a queue to perform a breadth-first search for the minimum number of coins
    queue = deque([(0, 0)])  # (current sum, number of coins used)
    visited = set([0])
    
    while queue:
        current_sum, num_coins = queue.popleft()
        
        if current_sum == S:
            return num_coins
        
        for coin in coins:
            new_sum = current_sum + (coin[0]**2 + coin[1]**2)
            if new_sum <= S and new_sum not in visited:
                visited.add(new_sum)
                queue.append((new_sum, num_coins + 1))
    
    return float('inf')

def main():
    n = int(input())
    
    for _ in range(n):
        m, S = map(int, input().split())
        coins = [tuple(map(int, input().split())) for _ in range(m)]
        result = min_coins(S, coins)
        print("not possible" if result == float('inf') else result)
        input()  # Consume the blank line

if __name__ == "__main__":
    main()