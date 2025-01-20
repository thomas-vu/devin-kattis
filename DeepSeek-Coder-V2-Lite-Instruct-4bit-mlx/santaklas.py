import math

# Function to calculate the distance from Santa Klas' current position to the ground
def distance_to_ground(altitude, angle):
    # Convert angle to radians
    angle_rad = math.radians(angle)
    # Calculate the distance using trigonometry
    return altitude / math.sin(angle_rad)

# Main function to determine the time or safety status
def main():
    # Read input values
    altitude, angle = map(int, input().split())
    
    # Check if the ship is heading for the ground or not
    if angle == 0 or angle == 180:
        print("safe")
    else:
        # Calculate the distance to the ground
        dist_to_ground = distance_to_ground(altitude, math.radians(angle))
        # Calculate the time to reach the ground
        time_to_ground = int(dist_to_ground)
        # Output the result
        print(time_to_ground)

# Call the main function
main()