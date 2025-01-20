# Read input
N, Q = map(int, input().split())
events = [input().split() for _ in range(Q)]

# Initialize the wealth of each person to 0 kroners
wealth = [0] * N
last_restart = -1

# Process each event
for i, event in enumerate(events):
    command = event[0]
    
    if command == 'SET':
        person, amount = int(event[1]) - 1, int(event[2])
        wealth[person] = amount
    elif command == 'RESTART':
        last_restart = int(event[1])
        wealth = [last_restart] * N
    elif command == 'PRINT':
        person = int(event[1]) - 1
        print(wealth[person] if last_restart == -1 else last_restart)