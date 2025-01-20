import math

def f(x):
    return 10 * math.sqrt(x)

def apply_curve(x, k):
    score = x
    for _ in range(k):
        score = f(score)
    return math.ceil(score)

def main():
    x, y_low, y_high = map(int, input().split())
    
    min_k = float('inf')
    max_k = -1
    
    for k in range(101):  # Arbitrary large number of iterations to check for infinite curve
        curved_score = apply_curve(x, k)
        if y_low <= curved_score <= y_high:
            min_k = min(min_k, k)
            max_k = max(max_k, k)
        if curved_score > y_high:
            break
    
    if min_k == float('inf'):
        print("impossible")
    else:
        if max_k == 100:
            print("inf")
        else:
            print(min_k, max_k)

if __name__ == "__main__":
    main()