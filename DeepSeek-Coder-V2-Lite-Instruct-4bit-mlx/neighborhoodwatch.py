N, K = map(int, input().split())
watch_houses = [int(input()) for _ in range(K)]

# Initialize the safety rating to 0
safety_rating = 0

# Iterate over each house on the street
for i in range(1, N + 1):
    # Check if the current house can be reached from any watch house
    for watch_house in watch_houses:
        if i <= watch_house or (i - watch_house) % 2 == 1:
            safety_rating += 1
            break

print(safety_rating)