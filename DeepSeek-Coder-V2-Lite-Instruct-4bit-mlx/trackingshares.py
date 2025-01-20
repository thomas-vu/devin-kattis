def main():
    C = int(input())
    companies_data = []
    
    for _ in range(C):
        K = int(input())
        company_data = {}
        for _ in range(K):
            N, D = map(int, input().split())
            company_data[D] = N
        companies_data.append(company_data)
    
    all_days = set()
    for company_data in companies_data:
        all_days.update(company_data.keys())
    
    total_shares = {}
    for day in sorted(all_days):
        shares = 0
        for company_data in companies_data:
            if day in company_data:
                shares += company_data[day]
        total_shares[day] = shares
    
    result = [total_shares[day] for day in sorted(total_shares.keys())]
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()