import math

def min_distance(W):
    # Define the positions of Agneta and Beata over time
    t = W / 2.0  # Time for Agneta to complete one revolution
    
    # Calculate the positions of Agneta and Beata at time t
    x_agneta = math.cos(t) + (W / 2.0 - t) * math.sin(t)
    y_agneta = math.sin(t) - (W / 2.0 - t) * math.cos(t)
    
    x_beata = 1 + math.cos(W / 2.0)
    y_beata = math.sin(W / 2.0)
    
    # Calculate the Euclidean distance between Agneta and Beata at time t
    dist = math.sqrt((x_agneta - x_beata)**2 + (y_agneta - y_beata)**2)
    
    return dist

# Read the input
W = float(input().strip())

# Calculate and print the result
result = min_distance(W)
print("{:.10f}".format(result))