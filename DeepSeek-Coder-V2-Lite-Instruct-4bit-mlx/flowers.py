import math

def calculate_volume(a, b, h):
    volume = 0
    for x in range(int(h)):
        y = a * math.exp(-x**2) + b * math.sqrt(x)
        volume += math.pi * y**2
    return volume

V, N = map(float, input().split())
best_fit_index = -1
min_difference = float('inf')

for i in range(int(N)):
    a, b, h = map(float, input().split())
    volume = calculate_volume(a, b, h)
    difference = abs(volume - V)
    
    if difference < min_difference:
        min_difference = difference
        best_fit_index = i

print(best_fit_index)