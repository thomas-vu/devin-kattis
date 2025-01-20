def can_acquire_infinite_emeralds(villagers, trades):
    # Create a map to store the number of each item needed for each villager
    need_map = {i: {} for i in range(len(villagers))}
    
    # Parse the trades and populate the need_map
    for villager, trade in enumerate(trades):
        for t in trade:
            a1, s1, a2, s2 = t.split()
            a1, a2 = int(a1), int(a2)
            if s1 not in need_map[villager]:
                need_map[villager][s1] = 0
            if s2 not in need_map[villager]:
                need_map[villager][s2] = 0
            need_map[villager][s1] -= a1
            need_map[villager][s2] += a2
    
    # Check if we can acquire infinite emeralds
    for item, count in need_map[0].items():
        if item != "Emerald" and count > 0:
            return "no"
    return "yes"

# Main function to read input and process the solution
def main():
    N = int(input().strip())
    trades = [[] for _ in range(N)]
    for i in range(N):
        t = int(input().strip())
        trades[i] = [input().strip() for _ in range(t)]
    print(can_acquire_infinite_emeralds(N, trades))

if __name__ == "__main__":
    main()