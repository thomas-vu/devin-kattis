import sys

def main():
    n, t = map(int, input().split())
    demands = []
    total_demand = 0
    
    for _ in range(n):
        a, b, d = map(int, input().split())
        demands.append((a, b, d))
        total_demand += d
    
    fair_shares = [t * (d / total_demand) for a, b, d in demands]
    bandwidths = [a if fair_shares[i] < a else b if fair_shares[i] > b else fair_shares[i] for i in range(n)]
    
    # Calculate the sum of squared errors
    total_bandwidth = sum(bandwidths)
    if abs(total_bandwidth - t) > 1e-6:
        raise ValueError("Sum of allocated bandwidth does not match total bandwidth")
    
    for bw in bandwidths:
        print("{:.8f}".format(bw))

if __name__ == "__main__":
    main()