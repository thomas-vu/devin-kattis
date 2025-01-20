w, h = map(int, input().split())
n, m = map(int, input().split())
asteroids = [tuple(map(int, input().split())) for _ in range(n)]
destinations = [tuple(map(int, input().split())) for _ in range(m)]

def is_safe(x_r, y_r, w, h):
    for x_a, y_a, r_a in asteroids:
        # Calculate the distance between the center of the asteroid and the nearest point on the rectangle
        dx = max(x_r, min(x_a + r_a, x_r + w)) - min(x_r, max(x_a - r_a, x_r))
        dy = max(y_r, min(y_a + r_a, y_r + h)) - min(y_r, max(y_a - r_a, y_r))
        distance = dx**2 + dy**2
        
        # If the square of the distance is less than or equal to the sum of the radii squared, there's an overlap
        if distance <= (r_a + min(w, h))**2:
            return "DOOMSLUG STOP!"
    return "DOOMSLUG GO!"

for dest in destinations:
    print(is_safe(*dest))