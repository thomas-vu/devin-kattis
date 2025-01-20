def rain_fall(L, K, T1, T2, H):
    # Calculate the net height of water in the tube after time T2
    net_height = H - L
    
    # Calculate the amount of water lost due to leak in time T2
    water_lost = K * (T1 + T2)
    
    # Calculate the net rainfall based on the net height of water after time T2
    net_rainfall = max(0, net_height - water_lost) / (T1 + T2)
    
    # Calculate the total rainfall based on the observed water level after time T2
    total_rainfall = (H / net_rainfall) if net_rainfall != 0 else float('inf')
    
    # Calculate the smallest and largest possible rainfall rates
    min_rainfall = net_rainfall * (T1 / (T1 + T2))
    max_rainfall = total_rainfall
    
    return min_rainfall, max_rainfall

# Read input from stdin
L, K, T1, T2, H = map(float, input().split())

# Calculate and print the result
F1, F2 = rain_fall(L, K, T1, T2, H)
print("{:.6f} {:.6f}".format(F1, F2))