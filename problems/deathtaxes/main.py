def main():
    shares = []
    avg_cost = 0
    
    while True:
        try:
            event = input().strip()
            if event.startswith("buy"):
                x, y = map(int, event.split()[1:])
                shares.append(x)
                avg_cost += x * y
            elif event.startswith("sell"):
                x, y = map(int, event.split()[1:])
                avg_cost -= x * y / shares[-1] if shares else 0
            elif event.startswith("split"):
                x = int(event.split()[1])
                shares[-1] *= x
            elif event.startswith("merge"):
                x = int(event.split()[1])
                shares[-1] //= x
            elif event.startswith("die"):
                price = float(event.split()[1])
                total_shares = sum(shares)
                capital_gain = (price - avg_cost / total_shares * sum(shares)) * shares[-1]
                tax = capital_gain * 0.3
                final_amount = (total_shares - sum(shares)) * (price - tax)
                print("{:.2f}".format(final_amount))
                break
        except EOFError:
            break

if __name__ == "__main__":
    main()