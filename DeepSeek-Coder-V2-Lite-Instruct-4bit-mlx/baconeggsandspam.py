def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        orders = {}
        for _ in range(n):
            line = input().split()
            name = line[0]
            items = line[1:]
            
            for item in items:
                if item not in orders:
                    orders[item] = set()
                orders[item].add(name)
        
        sorted_items = sorted(orders.keys())
        for item in sorted_items:
            names = sorted(orders[item])
            print(f"{item} {' '.join(names)}")
        print()

if __name__ == "__main__":
    main()