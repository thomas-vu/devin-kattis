import math

def calculate_area(x, y, w, h, v):
    # Convert angle from degrees to radians
    theta = math.radians(v)
    # Calculate the corners of the board in rotated coordinate system
    top_left = (x - w / 2, y + h / 2)
    top_right = (x + w / 2, y + h / 2)
    bottom_right = (x + w / 2, y - h / 2)
    bottom_left = (x - w / 2, y - h / 2)
    
    # Rotate the corners back to the original coordinate system
    top_left = rotate(top_left[0], top_left[1], theta, x, y)
    top_right = rotate(top_right[0], top_right[1], theta, x, y)
    bottom_right = rotate(bottom_right[0], bottom_right[1], theta, x, y)
    bottom_left = rotate(bottom_left[0], bottom_left[1], theta, x, y)
    
    # Calculate the bounding box of the rotated board
    min_x = min(top_left[0], top_right[0], bottom_right[0], bottom_left[0])
    max_x = max(top_left[0], top_right[0], bottom_right[0], bottom_left[0])
    min_y = min(top_left[1], top_right[1], bottom_right[1], bottom_left[1])
    max_y = max(top_left[1], top_right[1], bottom_right[1], bottom_left[1])
    
    # Calculate the area of the bounding box
    width = max_x - min_x
    height = max_y - min_y
    
    return width * height

def rotate(x, y, theta, pivot_x, pivot_y):
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    new_x = (x - pivot_x) * cos_theta - (y - pivot_y) * sin_theta + pivot_x
    new_y = (x - pivot_x) * sin_theta + (y - pivot_y) * cos_theta + pivot_y
    return (new_x, new_y)

def main():
    N = int(input())
    for _ in range(N):
        n = int(input())
        total_area = 0
        occupied_area = 0
        for _ in range(n):
            x, y, w, h, v = map(float, input().split())
            board_area = w * h
            occupied_area += calculate_area(x, y, w, h, v)
            total_area += board_area
        fraction = (occupied_area / total_area) * 100
        print(f"{fraction:.1f} %")

if __name__ == "__main__":
    main()