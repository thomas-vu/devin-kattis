def min_payment(price, denominations):
    total = sum(denominations)
    change = total - price
    denominations.sort(reverse=True)
    
    count = 0
    for coin in denominations:
        if change >= coin:
            count += 1
            change -= coin
    
    return total, count

def main():
    t = int(input())
    for _ in range(t):
        price = int(input())
        n = int(input())
        denominations = [int(input()) for _ in range(n)]
        total, count = min_payment(price, denominations)
        print(total, count)

if __name__ == "__main__":
    main()