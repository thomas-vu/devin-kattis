def minimum_payments(R, B, M):
    R /= 100.0
    payments = 0
    while B > 0:
        monthly_interest = (R * B + 0.005) // 1
        if monthly_interest >= M:
            return "impossible"
        B += monthly_interest
        if B <= M:
            return payments + 1
        B -= M
        payments += 1
    return payments

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    test_cases = int(data[index])
    index += 1
    results = []
    
    for _ in range(test_cases):
        R = float(data[index])
        B = float(data[index + 1])
        M = float(data[index + 2])
        index += 3
        result = minimum_payments(R, B, M)
        results.append(result)
    
    for result in results:
        print(result)

main()