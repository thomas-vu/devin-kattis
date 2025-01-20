def can_distribute_equally(n, prizes):
    total_prize = sum(prizes)
    if total_prize % 3 != 0:
        return "no"
    
    equal_share = total_prize // 3
    count_ways = [0] * 4
    
    current_sum = 0
    for prize in prizes:
        current_sum += prize
        if current_sum % 3 == 0:
            count_ways[1] += 1
        elif current_sum % 3 == 1:
            count_ways[2] += 1
        elif current_sum % 3 == 2:
            count_ways[3] += 1
    
    if count_ways[1] == 0 or count_ways[2] == 0:
        return "no"
    
    return "yes"

# Read input from stdin
n = int(input().strip())
prizes = list(map(int, input().strip().split()))

# Output the result
print(can_distribute_equally(n, prizes))