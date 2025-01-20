import sys
input = sys.stdin.readline

def calculate_revolutions(r):
    # The circumference of Sanic's circle (radius 1) is 2 * pi
    # The circumference of the loop's circle (radius r) is 2 * pi * r
    # To make one complete lap, Sanic needs to travel the distance of the loop's circumference
    # The number of revolutions is the ratio of the loop's circumference to Sanic's circumference
    return (2 * 3.141592653589793) / (2 * 3.141592653589793 * r)

# Read the input
r = float(input().strip())

# Calculate and print the number of revolutions
x = calculate_revolutions(r)
print("{:.6f}".format(x))