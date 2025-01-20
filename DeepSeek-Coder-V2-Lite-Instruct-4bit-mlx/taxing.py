def calculate_gift(B, tax_bands, P, F, friends):
    # Calculate the total amount after tax for each friend based on given rules
    def calculate_after_tax(earnings, target):
        remaining = earnings - target
        tax_amount = 0.0
        for i in range(B):
            band, rate = tax_bands[i]
            if remaining > 0:
                taxable = min(remaining, band)
                tax_amount += taxable * (rate / 100.0)
                remaining -= taxable
        if remaining > 0:
            tax_amount += remaining * (P / 100.0)
        return target + tax_amount

    # Calculate the amount George should give to each friend before tax
    for earning, target in friends:
        pre_tax = calculate_after_tax(earning, target)
        print("{:.6f}".format(pre_tax))

# Read input from stdin
B = int(input())
tax_bands = []
for _ in range(B):
    s, p = map(float, input().split())
    tax_bands.append((s, p))
P = float(input())
F = int(input())
friends = []
for _ in range(F):
    e, m = map(float, input().split())
    friends.append((e, m))

# Calculate and print the result
calculate_gift(B, tax_bands, P, F, friends)