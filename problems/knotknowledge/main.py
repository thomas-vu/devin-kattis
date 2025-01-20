def find_remaining_knot(n, needed_to_learn, learned):
    combined = set(needed_to_learn) | set(learned)
    for knot in needed_to_learn:
        if knot not in combined:
            return knot

n = int(input())
needed_to_learn = list(map(int, input().split()))
learned = list(map(int, input().split()))
print(find_remaining_knot(n, needed_to_learn, learned))