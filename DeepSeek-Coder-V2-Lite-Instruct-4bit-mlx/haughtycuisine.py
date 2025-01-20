import random

n = int(input())
menus = []
for _ in range(n):
    line = input().split()
    d = int(line[0])
    dishes = line[1:]
    menus.append(dishes)

# Randomly select a menu
selected_menu = random.choice(menus)

m = len(selected_menu)
print(m)
for dish in selected_menu:
    print(dish)