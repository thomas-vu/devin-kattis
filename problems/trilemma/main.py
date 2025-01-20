def classify_triangle(x1, y1, x2, y2, x3, y3):
    # Calculate the lengths of the sides
    a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    c = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
    
    # Check if the points form a triangle
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "not a triangle"
    
    # Check the type of triangle by angles
    cosA = ((b**2 + c**2 - a**2) / (2 * b * c))
    cosB = ((a**2 + c**2 - b**2) / (2 * a * c))
    cosC = ((a**2 + b**2 - c**2) / (2 * a * b))
    
    if cosA == 0:
        angleA = "right"
    elif cosA < 0:
        angleA = "obtuse"
    else:
        angleA = "acute"
    
    if cosB == 0:
        angleB = "right"
    elif cosB < 0:
        angleB = "obtuse"
    else:
        angleB = "acute"
    
    if cosC == 0:
        angleC = "right"
    elif cosC < 0:
        angleC = "obtuse"
    else:
        angleC = "acute"
    
    # Check the type of triangle by sides
    if a == b and b == c:
        return f"isosceles {angleA} triangle" if angleA == "right" else f"isosceles {angleC} triangle"
    elif a != b and b != c and a != c:
        return f"scalene {angleA} triangle" if angleA == "right" else f"scalene {angleC} triangle"
    else:
        return f"isosceles {angleA} triangle" if angleA == "right" else f"isosceles {angleC} triangle"
    
    # This point should never be reached because the above conditions cover all possibilities
    return "not a triangle"

# Main function to read input and output results
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    results = []
    
    for i in range(1, N + 1):
        x1, y1, x2, y2, x3, y3 = map(int, data[i*3-2:i*3+1])
        results.append(f"Case #{i}: {classify_triangle(x1, y1, x2, y2, x3, y3)}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()