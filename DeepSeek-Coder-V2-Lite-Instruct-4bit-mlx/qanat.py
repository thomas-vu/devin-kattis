import math

def calculate_cost(w, h, n):
    # Calculate the minimum excavation cost for a given configuration of shafts
    shafts = [0.0] * n
    step = w / (n + 1)
    for i in range(n):
        shafts[i] = (i + 1) * step
    total_cost = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            total_cost += math.sqrt((shafts[j] - shafts[i])**2 + h**2)
    for i in range(n):
        total_cost += shafts[i] * math.sqrt(1 + h**2)
    total_cost += w * h / 2.0
    return total_cost

def main():
    w, h, n = map(int, input().split())
    cost = calculate_cost(w, h, n)
    print("{:.6f}".format(cost))
    
    shafts = [0.0] * n
    step = w / (n + 1)
    for i in range(n):
        shafts[i] = (i + 1) * step
    
    if n > 10:
        for i in range(10):
            print("{:.6f}".format(shafts[i]))
    else:
        for i in range(n):
            print("{:.6f}".format(shafts[i]))

if __name__ == "__main__":
    main()