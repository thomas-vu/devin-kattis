def find_orders(menu, target):
    n = len(menu)
    results = []
    
    def backtrack(start, remain, path):
        if remain == 0:
            results.append(path[:])
            return
        for i in range(start, n):
            if menu[i] <= remain:
                path.append(i + 1)  # +1 because the item index is 1-based
                backtrack(i, remain - menu[i], path)
                path.pop()
            else:
                break
    
    backtrack(0, target, [])
    return results

def main():
    n = int(input())
    menu = list(map(int, input().split()))
    m = int(input())
    orders = [int(input()) for _ in range(m)]
    
    for target in orders:
        results = find_orders(menu, target)
        if len(results) == 1:
            print(' '.join(map(str, results[0])))
        elif len(results) > 1:
            print('Ambiguous')
        else:
            print('Impossible')

if __name__ == "__main__":
    main()