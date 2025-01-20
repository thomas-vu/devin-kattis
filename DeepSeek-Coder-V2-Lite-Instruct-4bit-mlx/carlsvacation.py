import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def main():
    x1, y1, x2, y2, h1 = map(int, input().split())
    x3, y3, x4, y4, h2 = map(int, input().split())
    
    # Find the base centers and apex points of both pyramids
    x1b = (x1 + x2) / 2
    y1b = (y1 + y2) / 2
    x3a = (x3 + x4) / 2
    y3a = (y3 + y4) / 2
    
    # Calculate the distance between base centers
    d = distance(x1b, y1b, x3a, y3a)
    
    # Calculate the angles of the pyramids
    angle1 = math.atan2(y2 - y1, x2 - x1)
    angle2 = math.atan2(y4 - y3, x4 - x3)
    
    # Calculate the vertical distances from apex to base center
    h1_vertical = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) / 2
    h2_vertical = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2) / 2
    
    # Calculate the angles from apex to base center
    angle1_to_center = math.atan2(y1b - y1, x1b - x1)
    angle2_to_center = math.atan2(y3a - y3, x3a - x3)
    
    # Calculate the distance between apex points using law of cosines
    d2 = (h1 + h2) ** 2 - 2 * (h1 + h2) ** 2 * math.cos(angle1 - angle2)
    d_final = math.sqrt(d2 + (h1 - h2) ** 2)
    
    print("{:.10f}".format(d_final))

if __name__ == "__main__":
    main()