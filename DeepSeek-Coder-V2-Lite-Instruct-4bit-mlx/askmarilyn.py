def play_game():
    for _ in range(1000):
        # Initial choice of door
        print('A')
        
        # Interaction with Marilyn
        response = input().split()
        opened_door = response[0]
        bottles_behind_door = int(response[1])
        
        # Determine the door to switch to
        if bottles_behind_door == 0:
            # If the opened door has no bottle, switch to the other door
            final_choice = 'C' if opened_door == 'A' else 'A'
        else:
            # If the opened door has a bottle, stick with your initial choice or switch to the other door
            final_choice = 'B' if opened_door == 'A' else ('C' if opened_door == 'B' else 'A')
        
        # Output the final choice of door
        print(final_choice)

# Run the game
play_game()