def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    L = int(data[index + 1])
    P = int(data[index + 2])
    index += 3
    
    passengers = [int(data[index + i]) for i in range(P)]
    index += P
    
    max_distance = 0
    car_counts = [0] * N
    
    for passenger in passengers:
        closest_car = 0
        min_distance = float('inf')
        
        for car in range(N):
            door_distance = abs((car * (L / 2)) - passenger) + (L / 2)
            if door_distance < min_distance:
                min_distance = door_distance
                closest_car = car + 1
            elif door_distance == min_distance and (car + 1) > closest_car:
                closest_car = car + 1
        
        max_distance = max(max_distance, min_distance)
        car_counts[closest_car - 1] += 1
    
    print(max_distance)
    print(max(car_counts))

if __name__ == "__main__":
    main()