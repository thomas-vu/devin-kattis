n, k = map(int, input().split())
bags = list(map(int, input().split()))

# Find the position of Benni's bag in the list
bennis_position = bags.index(k) + 1

# Determine the position in terms of "fyrst" or "naestfyrst"
if bennis_position == 1:
    print("fyrst")
elif bennis_position == 2:
    print("naestfyrst")
else:
    print(bennis_position - 1, "naestfyrst")