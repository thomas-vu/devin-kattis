def find_meeting_point(ascents, descents):
    total_time = 0
    for ascent in ascents:
        total_time += ascent[1]
    for descent in descents:
        total_time += descent[1]
    
    ascent_distance = [0] * (len(ascents) + 1)
    descent_distance = [0] * (len(descents) + 1)
    
    for i in range(len(ascents)):
        ascent_distance[i+1] = ascent_distance[i] + ascents[i][0]
    
    for i in range(len(descents)):
        descent_distance[i+1] = descent_distance[i] + descents[i][0]
    
    for i in range(1, len(ascents) + 1):
        for j in range(1, len(descents) + 1):
            if ascent_distance[i] == descent_distance[j]:
                return (ascent_distance[i] / ascents[i-1][1]) * total_time
    
    return -1

a, d = map(int, input().split())
ascents = [list(map(int, input().split())) for _ in range(a)]
descents = [list(map(int, input().split())) for _ in range(d)]

result = find_meeting_point(ascents, descents)
print("{:.6f}".format(result))