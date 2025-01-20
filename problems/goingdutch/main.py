def min_transactions(M, receipts):
    balances = [0] * M
    for a, b, p in receipts:
        balances[a] -= p
        balances[b] += p
    
    positive_balances = sorted([bal for bal in balances if bal > 0], reverse=True)
    negative_balances = sorted([-bal for bal in balances if bal < 0], reverse=True)
    
    transactions = 0
    while positive_balances and negative_balances:
        if positive_balances[-1] >= -negative_balances[-1]:
            bal = positive_balances.pop()
            neg_bal = negative_balances.pop()
            bal += neg_bal
        else:
            neg_bal = negative_balances.pop()
            bal = positive_balances.pop()
        transactions += 1
        if bal != 0:
            positive_balances.append(bal)
    
    return transactions

def main():
    while True:
        try:
            line = input().strip()
            if not line:
                continue
            M, N = map(int, line.split())
            receipts = [list(map(int, input().strip().split())) for _ in range(N)]
            print(min_transactions(M, receipts))
        except EOFError:
            break

if __name__ == "__main__":
    main()