def max_blue_lemonade(N, trades):
    from fractions import Fraction
    
    # Initialize the amount of pink lemonade we have and a list to store the maximum blue lemonade we can get from each child
    pink_lemonade = Fraction(1)
    max_blue = [Fraction(0)] * N
    
    # Process each trade from the end to the beginning (since we can't walk back)
    for i in range(N-1, -1, -1):
        offer_lemonade, want_lemonade, exchange_rate = trades[i]
        # Calculate the maximum blue lemonade we can get from this trade
        if offer_lemonade == "pink":
            max_blue[i] = Fraction(exchange_rate) * pink_lemonade
        else:
            # If we have already calculated the max blue for this child's trade, use it
            if i < N-1:
                max_blue[i] = Fraction(exchange_rate) * (pink_lemonade + max_blue[i+1]) / (exchange_rate - 1)
            else:
                # If it's the last child, calculate directly
                max_blue[i] = Fraction(exchange_rate) * pink_lemonade / (exchange_rate - 1)
        # Update the amount of pink lemonade after this trade
        pink_lemonade -= Fraction(1) / exchange_rate
    
    # The final answer is the maximum blue lemonade we can get from any child, limited to 10 liters
    return min(float(max_blue[0]), 10)

# Read input
N = int(input())
trades = [input().split() for _ in range(N)]
for i in range(N):
    trades[i][2] = float(trades[i][2])

# Calculate and output the result
result = max_blue_lemonade(N, trades)
print("{:.15f}".format(result))