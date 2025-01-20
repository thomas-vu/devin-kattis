import sys
from math import inf

# Read the number of phones
n = int(sys.stdin.readline().strip())

# Read the phone specifications
phones = []
for i in range(n):
    x_i, y_i, z_i = map(int, sys.stdin.readline().strip().split())
    phones.append((x_i, y_i, z_i))

# Function to calculate the opportunity cost of a phone
def opportunity_cost(x, y, z, phones):
    max_cost = 0
    min_index = -1
    for phone in phones:
        cost = max(phone[0] - x, 0) + max(phone[1] - y, 0) + max(phone[2] - z, 0)
        if cost > max_cost or (cost == max_cost and phone < (min_index, min_index) in phones):
            max_cost = cost
            min_index = phone
    return max_cost, min_index

# Find the phone with the minimum opportunity cost
min_cost, best_phone = inf, ()
for i in range(n):
    cost, phone = opportunity_cost(phones[i][0], phones[i][1], phones[i][2], phones)
    if cost < min_cost:
        min_cost = cost
        best_phone = phone

# Output the result
print(min_cost, phones.index(best_phone) + 1)