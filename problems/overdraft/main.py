def min_starting_balance(transactions):
    balance = 0
    min_balance = 0
    for transaction in transactions:
        balance += transaction
        if balance < min_balance:
            min_balance = balance
    return -min_balance

# Read input
n = int(input())
transactions = [int(input()) for _ in range(n)]

# Calculate and output the result
print(min_starting_balance(transactions))