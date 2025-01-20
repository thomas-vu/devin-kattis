previous_hash = 140000000
transaction_a = "charlie-pays-to-eve-9-sg-coins"
token_a = 218216710
hash_value_a = (previous_hash * 31 + len(transaction_a)) % 1000000007
hash_value_a = (hash_value_a * 7 + token_a) % 1000000007
print(f"{transaction_a} {token_a}")

# Calculate the next hash value for block B
transaction_b = "icpc-sg-2018-at-nus"
token_b = 620658977
hash_value_b = (hash_value_a * 31 + len(transaction_b)) % 1000000007
hash_value_b = (hash_value_b * 7 + token_b) % 1000000007
print(f"{transaction_b} {token_b}")