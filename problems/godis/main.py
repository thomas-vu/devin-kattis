def max_candy(bags):
    candy_count = {i: 0 for i in range(-10, 11) if i != 0}
    
    for bag in bags:
        types = {}
        for i in range(0, len(bag), 2):
            type_candy = bag[i]
            count = bag[i + 1]
            types[type_candy] = count
        
        for type_candy, count in types.items():
            if -type_candy not in types:
                candy_count[type_candy] += count
    
    return sum(candy_count.values())

# Read input
N = int(input().strip())
bags = []
for _ in range(N):
    bag = list(map(int, input().strip().split()))
    bags.append(bag)

# Calculate and print the result
print(max_candy(bags))