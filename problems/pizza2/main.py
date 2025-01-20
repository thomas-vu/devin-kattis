import sys
R, C = map(int, input().split())
cheese_area = (R**2 - (R-C)**2)*3.141592653589793
total_area = R**2*3.141592653589793
cheese_percentage = (cheese_area / total_area) * 100
print("{:.12f}".format(cheese_percentage))