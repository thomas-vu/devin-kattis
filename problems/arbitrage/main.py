import sys

def find_arbitrage(currencies, exchange_rates):
    # Create a graph where each currency is a node and each exchange rate is an edge with weight
    graph = {currency: [] for currency in currencies}
    for rate in exchange_rates:
        src, dest, a, b = rate
        graph[src].append((dest, float(a) / float(b)))
    
    # Use Bellman-Ford to detect negative cycles (arbitrage)
    dist = {currency: float('inf') for currency in currencies}
    dist[currencies[0]] = 1.0
    
    for _ in range(len(currencies) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if dist[node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[node] + weight
    
    # Check for negative cycle
    for node in graph:
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                return True  # Arbitrage found
    
    return False  # No arbitrage

def main():
    while True:
        C = int(sys.stdin.readline().strip())
        if C == 0:
            break
        
        currencies = sys.stdin.readline().strip().split()
        R = int(sys.stdin.readline().strip())
        
        exchange_rates = []
        for _ in range(R):
            rate = sys.stdin.readline().strip().split()
            exchange_rates.append((rate[0], rate[1], int(rate[2].split(':')[0]), int(rate[2].split(':')[1])))
        
        if find_arbitrage(currencies, exchange_rates):
            print("Arbitrage")
        else:
            print("Ok")

if __name__ == "__main__":
    main()