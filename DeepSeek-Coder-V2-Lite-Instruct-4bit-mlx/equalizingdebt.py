def main():
    n = int(input())
    debts = {}
    people = set()
    
    for _ in range(n):
        u, v, d = input().split()
        debts.setdefault(u, 0)
        debts[u] -= d
        debts.setdefault(v, 0)
        debts[v] += d
        people.add(u)
        people.add(v)
    
    for person in debts:
        if debts[person] != 0:
            continue
    
    transactions = []
    for person in debts:
        while debts[person] < 0:
            for debtor, amount in debts.items():
                if amount > 0 and debts[person] < 0:
                    min_d = min(-debts[person], amount)
                    debts[person] += min_d
                    debts[debtor] -= min_d
                    transactions.append((person, debtor, min_d))
    
    for person in people:
        while debts[person] > 0:
            for debtor, amount in debts.items():
                if amount < 0 and debts[person] > 0:
                    min_d = min(debts[person], -debts[debtor])
                    debts[person] -= min_d
                    debts[debtor] += min_d
                    transactions.append((person, debtor, -min_d))
    
    for transaction in transactions:
        print(*transaction)
    print("settled")

main()