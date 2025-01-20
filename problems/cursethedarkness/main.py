def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    m = int(data[index])
    index += 1
    results = []
    
    for _ in range(m):
        x_book, y_book = float(data[index]), float(data[index + 1])
        index += 2
        n = int(data[index])
        index += 1
        candles = [(float(data[index]), float(data[index + 1])) for _ in range(n)]
        index += n * 2
        
        light_a_candle = False
        for x_candle, y_candle in candles:
            if distance(x_book, y_book, x_candle, y_candle) <= 8:
                light_a_candle = True
                break
        
        results.append("light a candle" if light_a_candle else "curse the darkness")
    
    for result in results:
        print(result)

main()