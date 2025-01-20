G, T, N = map(int, input().split())
items_weights = list(map(int, input().split()))
total_weight_of_items = sum(items_weights)
remaining_towing_capacity = G - T
maximum_trailer_weight = int(0.9 * remaining_towing_capacity)
print(maximum_trailer_weight - total_weight_of_items)