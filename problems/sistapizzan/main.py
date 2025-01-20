def can_penny_guarantee_last_slice(n, pizzas):
    total_slices = sum(pizzas)
    if total_slices % 2 == 0:
        return "Nej"
    else:
        return "Ja"

# Read input
N = int(input())
pizzas = [int(input()) for _ in range(N)]

# Output the result
print(can_penny_guarantee_last_slice(N, pizzas))