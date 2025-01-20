def battle(ng, nm, godzilla_army, mechagodzilla_army):
    godzilla_army.sort()
    mechagodzilla_army.sort()
    
    while godzilla_army and mechagodzilla_army:
        if godzilla_army[0] < mechagodzilla_army[0]:
            godzilla_army.pop(0)
        elif mechagodzilla_army[0] < godzilla_army[0]:
            mechagodzilla_army.pop(0)
        else:
            godzilla_army.pop(0)
            mechagodzilla_army.pop(0)
    
    if godzilla_army:
        return "Godzilla"
    elif mechagodzilla_army:
        return "MechaGodzilla"
    else:
        return "uncertain"

T = int(input())
for _ in range(T):
    input()  # consume the blank line
    ng, nm = map(int, input().split())
    godzilla_army = list(map(int, input().split()))
    mechagodzilla_army = list(map(int, input().split()))
    
    result = battle(ng, nm, godzilla_army, mechagodzilla_army)
    print(result)