# Solution in Python 3
def find_numbers():
    low = 1
    high = 500
    
    for _ in range(10):
        mid = (low + high) // 2
        print(f"ASK {mid} {high}")
        result = input().split()
        if result[0] == "yes":
            low = max(low, mid + 1)
        else:
            high = min(high, mid)
    
    print(f"GUESS {low} {high}")

find_numbers()