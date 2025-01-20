def cuckoo_clock(current_time, N):
    HH, MM = map(int, current_time.split(':'))
    count = 0
    
    while True:
        if MM == 0:
            count += HH
            if count > N:
                break
        elif MM % 15 == 0:
            count += 1
            if count > N:
                break
        
        MM += 1
        if MM == 60:
            HH += 1
            MM = 0
        if HH == 13:
            HH = 1
        
        if count == N:
            return f"{HH:02d}:{MM:02d}"

# Sample Input 1
print(cuckoo_clock("02:36", 10))  # Sample Output 1
# Expected Output: 102:45

# Sample Input 2
print(cuckoo_clock("12:00", 13))  # Sample Output 2
# Expected Output: 12:00

# Sample Input 3
print(cuckoo_clock("11:00", 30))  # Sample Output 3
# Expected Output: 01:00