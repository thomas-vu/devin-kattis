def classify_triangle(a, b, c):
    if a + b + c != 180:
        return "Invalid triangle"
    
    if a > 90 or b > 90 or c > 90:
        return "Trubbig Triangel"
    elif a < 90 and b < 90 and c < 90:
        return "Spetsig Triangel"
    elif a == 90 or b == 90 or c == 90:
        return "Ratvinklig Triangel"
    else:
        return "Invalid triangle"

# Read inputs from the user
a = int(input())
b = int(input())
c = int(input())

# Classify the triangle and print the result
result = classify_triangle(a, b, c)
print(result)