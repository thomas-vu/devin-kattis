def determine_winner(player1_cards, player2_cards):
    player1_power = sum([card_dict[card]['power'] for card in player1_cards])
    player2_power = sum([card_dict[card]['power'] for card in player2_cards])
    if player1_power > player2_power:
        return "Player 1"
    elif player2_power > player1_power:
        return "Player 2"
    else:
        return "Tie"

def main():
    global card_dict
    # Sample dictionary of cards with their abilities and power levels
    card_dict = {
        'Shadow Seraphina': {'ability': '', 'power': 5},
        'Voidclaw': {'ability': '', 'power': 3},
        'Vexia': {'ability': '', 'power': 2},
        'Ranger': {'ability': '', 'power': 4},
        'Anvil': {'ability': '', 'power': 6},
        'Seraphina': {'ability': '', 'power': 7},
        'Ironwood': {'ability': '', 'power': 8},
        'Guardian': {'ability': '', 'power': 9}
    }
    
    import sys
    input = sys.stdin.read
    data = input().split()
    
    left_location = []
    center_location = []
    right_location = []
    
    index = 0
    while index < len(data):
        left_line = data[index]
        center_line = data[index + 1]
        right_line = data[index + 2]
        index += 3
        
        left_cards = [] if left_line == '0' else data[index:index + int(left_line)].copy()
        index += int(left_line)
        
        center_cards = [] if center_line == '0' else data[index:index + int(center_line)].copy()
        index += int(center_line)
        
        right_cards = [] if right_line == '0' else data[index:index + int(right_line)].copy()
        index += int(right_line)
        
        left_location.append(left_cards)
        center_location.append(center_cards)
        right_location.append(right_cards)
    
    winner = determine_winner(left_location[0] + left_location[1], center_location[0] + center_location[1])
    if winner == "Tie":
        winner = determine_winner(right_location[0] + right_location[1], left_location[2] + left_location[3])
    if winner == "Tie":
        winner = determine_winner(center_location[2] + center_location[3], right_location[2] + right_location[3])
    
    print(winner)

main()