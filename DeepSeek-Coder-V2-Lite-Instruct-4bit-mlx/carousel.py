while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    offers = []
    for _ in range(n):
        a, b = map(int, input().split())
        offers.append((a, b))
    
    best_offer = None
    for _ in range(m):
        a, b = map(int, input().split())
        for offer in offers:
            if offer[0] <= a and (best_offer is None or best_offer[1] > offer[1]):
                best_offer = (a, b)
            elif offer[0] <= a and best_offer is not None and best_offer[1] == offer[1]:
                if best_offer[0] < offer[0]:
                    best_offer = (a, b)
    
    if best_offer is not None:
        print(f"Buy {best_offer[0]} tickets for ${best_offer[1]}")
    else:
        print("No suitable tickets offered")