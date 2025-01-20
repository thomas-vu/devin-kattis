def process_orders(n, orders):
    ask = float('inf')
    bid = 0
    stock = '-'
    results = []
    
    for i in range(n):
        order_type, x, y = orders[i].split()
        x = int(x)
        y = int(y)
        
        if order_type == 'buy':
            if x > bid:
                bid = x
                stock = y
        elif order_type == 'sell':
            if x < ask:
                ask = x
                stock = y
        
        if bid >= ask:
            stock = str(ask) + ' ' + str(bid) + ' ' + str(ask)
        else:
            stock = '-'
        
        results.append((str(ask), str(bid), str(stock)))
    
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        orders = data[index:index+n]
        index += n
        results.append(process_orders(n, orders))
    
    for result in results:
        for ask, bid, stock in result:
            print(ask, bid, stock)
        if _ != results.index(result):
            print()

if __name__ == "__main__":
    main()