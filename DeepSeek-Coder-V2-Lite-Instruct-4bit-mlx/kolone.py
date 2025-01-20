def swap_ants(row1, row2, T):
    # Convert the rows to lists for easier manipulation
    list1 = list(row1)
    list2 = list(row2)
    
    # Perform the swaps for T seconds
    for _ in range(T):
        if list1 and list2:
            # Swap the first ant in list1 with the first ant in list2
            list1[0], list2[0] = list2[0], list1[0]
            # Move the lists to simulate the next second
            list1 = [list2[0]] + list1[:-1]
            list2 = [list1[0]] + list2[:-1]
    
    # Convert the lists back to strings and return them
    return ''.join(list1) + ''.join(list2)

# Read input
N1, N2 = map(int, input().split())
row1 = input()
row2 = input()
T = int(input())

# Output the result after T seconds
result = swap_ants(row1, row2, T)
print(result)