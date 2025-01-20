N = int(input())
beverage = input()

for i in range(N, 0, -1):
    if i > 2:
        print(f"{i} bottles of {beverage} on the wall, {i} bottles of {beverage}.")
        print(f"Take one down, pass it around, {i-1} bottles of {beverage} on the wall.")
    elif i == 2:
        print(f"{i} bottles of {beverage} on the wall, {i} bottles of {beverage}.")
        print(f"Take one down, pass it around, 1 bottle of {beverage} on the wall.")
    else:
        print(f"{i} bottle of {beverage} on the wall, {i} bottle of {beverage}.")
        print("Take it down, pass it around, no more bottles of {beverage}.")