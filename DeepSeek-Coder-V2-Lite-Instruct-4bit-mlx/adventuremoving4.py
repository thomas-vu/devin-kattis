def min_cost_gas(distance, gas_stations):
    tank = 100  # Initial tank is half full (200/2)
    cost = 0
    
    for i in range(len(gas_stations)):
        if tank == 0:
            return "Impossible"
        
        # Drive to the next gas station or destination
        if i < len(gas_stations) - 1:
            next_station = gas_stations[i + 1]
        else:
            next_station = distance
        
        travel_distance = next_station - gas_stations[i][0]
        
        # Calculate the amount of gas needed for the travel distance
        if tank < travel_distance:
            refill = min(200, next_station - gas_stations[i][0])
            cost += refill * (gas_stations[i][1] / 10)
            tank = refill
        else:
            tank -= travel_distance
    
    # Ensure the tank is at least half full when reaching the destination
    if tank < 100:
        cost += (100 - tank) * (gas_stations[-1][1] / 10)
    
    return int(cost)

# Main function to read input and output the result
def main():
    distance = int(input())
    gas_stations = []
    
    while True:
        try:
            line = input()
            if not line:
                break
            distance_station, price_per_litre = map(int, line.split())
            gas_stations.append((distance_station, price_per_litre))
        except EOFError:
            break
    
    result = min_cost_gas(distance, gas_stations)
    print(result)

if __name__ == "__main__":
    main()