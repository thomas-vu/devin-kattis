city = input()
percentage = float(input())
n = int(input())
items = [input().strip() for _ in range(n)]

# Count the number of plastic items
plastic_count = sum(1 for item in items if item == "plast")
total_items = len(items)

# Determine if the bag is recyclable based on the percentage of plastic items
if (plastic_count / total_items) <= percentage:
    print("Jebb")
else:
    print("Neibb")