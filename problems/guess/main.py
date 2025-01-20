import sys

def binary_search():
    low, high = 1, 1000
    while low <= high:
        mid = (low + high) // 2
        print(mid)
        sys.stdout.flush()
        response = input().strip()
        if response == "correct":
            return
        elif response == "lower":
            high = mid - 1
        else:  # response is "higher"
            low = mid + 1

binary_search()