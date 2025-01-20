D = int(input())
R = int(input())
T = int(input())

# The number of candles in the right box should be R - D + T
correct_number = R - D + T
# The number of candles Rita needs to remove
candles_to_remove = R - correct_number

print(candles_to_remove)