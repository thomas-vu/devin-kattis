def min_crackers(k, m):
    low, high = 1, m
    while low < high:
        mid = (low + high) // 2
        if simulate_mailboxes(k, mid, m):
            high = mid
        else:
            low = mid + 1
    return low

def simulate_mailboxes(k, cracks, m):
    for _ in range(k):
        left, right = 1, m
        while left < right:
            mid = (left + right) // 2
            if simulate_single_mailbox(mid, cracks):
                right = mid
            else:
                left = mid + 1
        if left == m and not simulate_single_mailbox(m, cracks):
            return False
    return True

def simulate_single_mailbox(cracks, max_safe):
    if cracks > max_safe:
        return False
    else:
        return True

N = int(input())
for _ in range(N):
    k, m = map(int, input().split())
    result = min_crackers(k, m)
    print(result)