def best_card(G, S, C):
    buying_power = G * 3 + S * 2 + C * 1
    victory_points = 0
    
    if G > 0:
        victory_card = "Province"
        victory_points = 6
    elif S > 1 or (S == 1 and C >= 2) or (S == 0 and G > 0 and C > 1):
        victory_card = "Duchy"
        victory_points = 3
    elif C > 2 or (C == 2 and S > 0) or (C == 1 and G > 0):
        victory_card = "Estate"
        victory_points = 1
    else:
        victory_card = ""
    
    if buying_power >= 8:
        treasure_card = "Gold"
    elif buying_power >= 6:
        treasure_card = "Silver"
    else:
        treasure_card = "Copper"
    
    if victory_points > 0:
        return f"{victory_card} or {treasure_card}"
    else:
        return treasure_card

# Read input
G, S, C = map(int, input().split())

# Output the best card Jake can buy
print(best_card(G, S, C))