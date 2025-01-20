def check_items(N, items):
    required_items = ['keys', 'phone', 'wallet']
    forgotten_items = [item for item in required_items if item not in items]
    
    for item in forgotten_items:
        print(item)

# Sample Input 1
N = 4
items = ['jacket', 'gloves', 'wallet', 'keys']
check_items(N, items)
print()  # For the second sample input in the problem statement

# Sample Input 2
N = 4
items = ['phone', 'toque', 'wallet', 'keys']
check_items(N, items)
print()  # For the second sample input in the problem statement

# Sample Input 3
N = 5
items = ['scarf', 'jacket', 'gloves', 'snowpants', 'shades']
check_items(N, items)