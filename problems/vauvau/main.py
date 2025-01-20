a, b, c, d = map(int, input().split())
p, m, g = map(int, input().split())

def attack_dogs(arrival_time, a, b, c, d):
    cycle1 = a + b
    cycle2 = c + d
    
    time_in_cycle1 = arrival_time % cycle1
    time_in_cycle2 = arrival_time % cycle2
    
    if 1 <= time_in_cycle1 <= a and 1 <= time_in_cycle2 <= c:
        return 'both'
    elif 1 <= time_in_cycle1 <= a or 1 <= time_in_cycle2 <= c:
        return 'one'
    else:
        return 'none'

postman_result = attack_dogs(p, a, b, c, d)
milkman_result = attack_dogs(m, a, b, c, d)
garbage_man_result = attack_dogs(g, a, b, c, d)

print(postman_result)
print(milkman_result)
print(garbage_man_result)