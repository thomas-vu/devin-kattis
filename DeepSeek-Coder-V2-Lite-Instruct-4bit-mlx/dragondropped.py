import sys

# Read the number of locations from input
N = int(input())

# Initialize variables to simulate the process
current_location = 0
visited_locations = set()
requests_made = 0

# Function to simulate a request and get the response
def make_request(next_location):
    global current_location, visited_locations, requests_made
    if next_location == 0:
        sys.stdout.write("NEXT GABBY\n")
    elif next_location == 1:
        sys.stdout.write("NEXT SPIKE\n")
    elif next_location == -1:
        sys.stdout.write("RETURN GABBY\n")
    else:
        sys.stdout.write("RETURN SPIKE\n")
    sys.stdout.flush()
    
    s, e = map(int, input().split())
    requests_made += 1
    if s == 0:
        visited_locations.add(current_location)
    current_location = e
    return s, e

# Main loop to determine the ending location
while requests_made < 30000:
    if len(visited_locations) == N - 1 and requests_made >= 2:
        # We have visited all but one location, ask Spike to find out the last location
        sys.stdout.write("ASK SPIKE\n")
        sys.stdout.flush()
        s, e = map(int, input().split())
        if e == 1:
            sys.stdout.write(f"{e}\n")
            sys.stdout.flush()
            break
    else:
        # Visit the next location based on the current state
        if len(visited_locations) == N - 1:
            # If we have visited all but one location, ask Spike to return to the post office
            make_request(-1)
        else:
            next_location = 0 if len(visited_locations) % 2 == 0 else 1
            make_request(next_location)