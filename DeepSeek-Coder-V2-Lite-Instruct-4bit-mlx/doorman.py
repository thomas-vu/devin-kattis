X = int(input())
queue = input()

women_count = 0
men_count = 0
max_people = 0

for person in queue:
    if person == 'W':
        women_count += 1
    else:
        men_count += 1
    
    if abs(women_count - men_count) > X:
        break
    
    max_people += 1

print(max_people)