def calculate_scientific_points(cards):
    count = {'T': 0, 'C': 0, 'G': 0}
    for card in cards:
        count[card] += 1
    
    points = sum(value ** 2 for value in count.values()) + min(count.values()) * 7
    return points

# Read input from stdin
input_string = input().strip()
print(calculate_scientific_points(input_string))