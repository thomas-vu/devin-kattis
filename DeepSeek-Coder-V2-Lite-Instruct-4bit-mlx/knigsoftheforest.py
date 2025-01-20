k, n = map(int, input().split())
year_of_entry, strength = map(int, input().split())
mooses = []
for _ in range(n - 1):
    entry, str_val = map(int, input().split())
    mooses.append((entry, str_val))

# Sort the mooses based on their entry year
mooses.sort(key=lambda x: x[0])

# Determine the year Karl-Älgtav becomes the alpha-moose
for i in range(n - 1):
    if mooses[i][0] < year_of_entry and mooses[i][1] > strength:
        print("unknown")
        break
else:
    if i == n - 2 and mooses[i + 1][0] > year_of_entry:
        print(year_of_entry)