import sys

def main():
    n = int(sys.stdin.readline().strip())
    
    # Initialize the list to keep track of which switches control each light
    switch_control = [0] * n
    
    # Perform 32 queries to determine the mapping of switches to lights
    for _ in range(32):
        query = []
        # Ask about a random subset of switches
        for i in range(n):
            if switch_control[i] == 0:
                query.append(str(i + 1))
        
        if len(query) == 0:
            break
        
        # Output the query
        print("ASK", len(query), " ".join(query))
        sys.stdout.flush()
        
        # Read the response from the server
        response = list(map(int, sys.stdin.readline().strip().split()))
        
        # Update the switch_control list based on the response
        for i in range(n):
            if i + 1 in response:
                switch_control[i] = 1
    
    # Output the final answer after determining all mappings
    answer = " ".join(map(str, [i + 1 for i in range(n)]))
    print("ANSWER", answer)
    sys.stdout.flush()

if __name__ == "__main__":
    main()