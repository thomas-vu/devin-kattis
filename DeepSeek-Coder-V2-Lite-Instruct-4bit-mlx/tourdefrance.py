def compute_maximum_spread(front, rear):
    spreads = []
    for front_gear in front:
        for rear_gear in rear:
            spread = (rear_gear / front_gear)
            spreads.append(spread)
    spreads.sort()
    
    max_spread = 0
    for i in range(1, len(spreads)):
        spread_ratio = spreads[i] / spreads[i - 1]
        if spread_ratio > max_spread:
            max_spread = spread_ratio
    return max_spread

def main():
    while True:
        line = input()
        if line == '0':
            break
        front_sprockets = list(map(int, input().split()))
        rear_sprockets = list(map(int, input().split()))
        
        max_spread = compute_maximum_spread(front_sprockets, rear_sprockets)
        print("{:.2f}".format(max_spread))

if __name__ == "__main__":
    main()