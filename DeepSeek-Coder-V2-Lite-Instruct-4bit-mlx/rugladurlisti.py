n = int(input())
indices_asked = []
values_received = []

for _ in range(n):
    query = input().split()
    if query[0] == '?':
        k = int(query[1])
        indices_asked.append([int(x) for x in query[2:]])
    else:  # query[0] == '!'
        values_received = [int(x) for x in query[1:]]
        break

# Reconstruct the original list from the given indices and values
original_list = []
for asked, value in zip(indices_asked, values_received):
    for index in asked:
        if value[index - 1] not in original_list:
            original_list.append(value[index - 1])

# Output the reconstructed list in correct order
print('! ' + ' '.join(map(str, original_list)))