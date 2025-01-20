def read_ints():
    return list(map(int, input().split()))

def main():
    C = int(input())
    
    for case_num in range(1, C + 1):
        N, T = read_ints()
        E = int(input())
        
        towns = [0] * N
        drivers = []
        
        for _ in range(E):
            H, P = read_ints()
            if P > 0:
                drivers.append((H - 1, P))
            towns[H - 1] += 1
        
        if len(drivers) == 0:
            print(f"Case #{case_num}: IMPOSSIBLE")
        else:
            cars = [0] * N
            for i in range(N):
                min_cars = float('inf')
                for driver in drivers:
                    if driver[0] == i:
                        min_cars = min(min_cars, driver[1])
                cars[i] = min_cars
            
            total_drivers = sum(cars)
            if total_drivers < E:
                print(f"Case #{case_num}: IMPOSSIBLE")
            else:
                print(f"Case #{case_num}:", end=" ")
                for i in range(N):
                    if cars[i] > 0:
                        print(cars[i], end=" ")
                    else:
                        print("0", end=" ")
                print()

if __name__ == "__main__":
    main()