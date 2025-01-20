def parse_time(time_str):
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

def main():
    S = int(input())
    for x in range(1, S + 1):
        T = int(input())
        NA = int(input())
        NB = int(input())
        
        trips_AtoB = []
        trips_BtoA = []
        
        for _ in range(NA):
            depart, arrive = input().split()
            trips_AtoB.append((parse_time(depart), parse_time(arrive)))
        for _ in range(NB):
            depart, arrive = input().split()
            trips_BtoA.append((parse_time(depart), parse_time(arrive)))
        
        trips_AtoB.sort()
        trips_BtoA.sort()
        
        trains_at_A = 0
        trains_at_B = 0
        
        for trip in trips_AtoB:
            if trip[1] + T <= trip[0]:
                trains_at_A += 1
        
        for trip in trips_BtoA:
            if trip[1] + T <= trip[0]:
                trains_at_B += 1
        
        print(f"Case #{x}: {trains_at_A} {trains_at_B}")

if __name__ == "__main__":
    main()