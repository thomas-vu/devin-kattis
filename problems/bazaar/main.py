def calculate_difference(N, first_player_goods, second_player_goods):
    # Convert the lists to sets for easier manipulation
    first_set = set(first_player_goods)
    second_set = set(second_player_goods)
    
    # Calculate the initial values of pieces o' eight for both players
    first_value = sum([price for price in first_player_goods])
    second_value = sum([price for price in second_player_goods])
    
    # Play the game optimally by selling goods to maximize the difference
    for i in range(1, 2 * N + 1):
        if i in first_set:
            # First player sells a good priced i, increasing the price of another good
            first_value += (i - 1)
            # Remove the sold good from the player's set and update the value
            first_set.remove(i)
        elif i in second_set:
            # Second player sells a good priced i, increasing the price of another good
            second_value += (i - 1)
            # Remove the sold good from the player's set and update the value
            second_set.remove(i)
    
    # Return the difference between the values of pieces o' eight received by the first player and the second player
    return first_value - second_value

# Read input
N = int(input())
first_player_goods = list(map(int, input().split()))
second_player_goods = list(map(int, input().split()))

# Calculate and print the result
print(calculate_difference(N, first_player_goods, second_player_goods))