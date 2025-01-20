import math

def stirling_approximation(n):
    return math.sqrt(2 * math.pi * n) * (n ** n) / (math.e ** n)

while True:
    n = int(input())
    if n == 0:
        break
    actual_value = math.factorial(n)
    approx_value = stirling_approximation(n)
    ratio = actual_value / approx_value
    print("{:.12f}".format(ratio))