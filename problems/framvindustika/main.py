def progress_bar(p, w):
    completed = '#' * (p // (100 // w))
    remaining = '-' * (w - len(completed))
    return f"[{completed}{remaining}] |{p:>4}%"

# Example usage:
print(progress_bar(0, 10))    # [----------] |   0%
print(progress_bar(33, 10))   # [###-------] |  33%
print(progress_bar(25, 25))   # [######-------------------] |  25%
print(progress_bar(100, 20)) # [####################] | 100%