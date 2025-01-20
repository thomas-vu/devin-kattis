def main():
    N = int(input())
    K = int(input())
    
    store_items = {}
    for _ in range(K):
        i, S = input().split()
        i = int(i)
        if i not in store_items:
            store_items[i] = set()
        store_items[i].add(S)
    
    M = int(input())
    items_bought = [input().strip() for _ in range(M)]
    
    possible_paths = set([0])
    for item in items_bought:
        new_possible_paths = set()
        found = False
        for store in possible_paths:
            if item in store_items.get(store, set()):
                new_possible_paths.add(store)
                found = True
        if not found:
            print("impossible")
            return
        possible_paths = new_possible_paths
    
    if len(possible_paths) == 1:
        print("unique")
    else:
        print("ambiguous")

if __name__ == "__main__":
    main()