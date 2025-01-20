N = int(input())
people = []
for _ in range(N):
    line = list(map(int, input().split()))
    M_i = line[0]
    k = line[1]
    if k == 0:
        people.append({'M': M_i, 'I': float('inf'), 'send_to': []})
    else:
        send_to = [0] * N
        for j in range(2, 2 + k * 2, 2):
            person = line[j] - 1
            percent = line[j + 1] / 100.0
            send_to[person] = percent
        people.append({'M': M_i, 'I': 0, 'send_to': send_to})

# Calculate the initial number of envelopes sent to each person
for i in range(N):
    for j in range(N):
        if people[i]['send_to'][j] != 0:
            people[j]['I'] += people[i]['M'] * people[i]['send_to'][j]
            if people[j]['I'] > people[j]['M']:
                people[j]['I'] = people[j]['M']

# Check who is working at their maximum production speed
max_production = []
for i in range(N):
    if people[i]['I'] == people[i]['M']:
        max_production.append(str(i + 1))

print(' '.join(max_production))