def calculate_payout_ratio(a):
    b = 100 - a
    payout_one = (b / a) if a != 0 else float('inf')
    payout_two = (a / b) if b != 0 else float('inf')
    return payout_one, payout_two

a = int(input())
payout_one, payout_two = calculate_payout_ratio(a)
print("{:.10f}".format(payout_one))
print("{:.10f}".format(payout_two))