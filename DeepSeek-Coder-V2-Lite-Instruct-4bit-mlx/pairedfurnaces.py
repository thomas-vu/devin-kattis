n = int(input())
s = input()

# Count the number of on and off furnaces
on_count = s.count('1')
off_count = n - on_count

# Check if it's possible to turn all furnaces on
if on_count % 2 == 1:
    print("impossible")
else:
    # Turn on the necessary furnaces in pairs
    moves = 0
    toggle_count = 0
    for i in range(n):
        if s[i] == '1':
            toggle_count += 1
            if toggle_count % 2 == 0:
                moves += 1
    print(moves)