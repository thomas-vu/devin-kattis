def find_prescriptions(n, k, p):
    prescriptions = []
    for pills in range(1, int(k) + 1):
        if n % pills == 0 and (n // pills) <= p:
            prescriptions.append(pills)
    return prescriptions

# Read input
n, k, p = map(int, input().split())
prescriptions = find_prescriptions(n, k, p)
print(len(prescriptions))
for prescription in prescriptions:
    print(prescription)