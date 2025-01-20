import sys

def is_inside(x, y, rx, ry, w, h, r):
    # Adjust the click position to account for the rectangle's top-left corner
    x -= rx
    y -= ry
    
    # Check if the click is inside the corners (quarter circles)
    if x < r and y < r:
        return ((x - r) ** 2 + (y - r) ** 2) <= r**2
    elif x < r and y > h - r:
        return ((x - r) ** 2 + (y - (h - r)) ** 2) <= r**2
    elif x > w - r and y < r:
        return ((x - (w - r)) ** 2 + (y - r) ** 2) <= r**2
    elif x > w - r and y > h - r:
        return ((x - (w - r)) ** 2 + (y - (h - r)) ** 2) <= r**2
    # Check if the click is inside the rectangle without considering the corners
    elif x >= 0 and x <= w - r:
        if y >= 0 and y <= h - r:
            return True
    return False

def main():
    n = int(input())
    for _ in range(n):
        x, y, w, h, r = map(float, input().split())
        m = int(input())
        for _ in range(m):
            mx, my = map(float, input().split())
            if is_inside(mx, my, x, y, w, h, r):
                print("inside")
            else:
                print("outside")

if __name__ == "__main__":
    main()