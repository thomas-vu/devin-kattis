import sys

def main():
    input_lines = sys.stdin.read().strip()
    lines = input_lines.split('\n')
    index = 0
    
    def readline():
        nonlocal index
        line = lines[index]
        index += 1
        return line
    
    test_cases = int(readline())
    results = []
    
    for _ in range(test_cases):
        n, m = map(int, readline().split())
        houses = [int(readline()) for _ in range(m)]
        
        left, right = 0, max(houses)
        while left < right:
            mid = (left + right) / 2
            min_distance = float('inf')
            
            for house in houses:
                distance = abs(house - mid)
                if distance < min_distance:
                    min_distance = distance
            
            if n == 1:
                max_min_distance = min_distance
            else:
                left_child, right_child = mid - 1e-5, mid + 1e-5
                left_count = right_count = 0
                for house in houses:
                    if house < left_child and (house - 0) / min_distance <= 1:
                        left_count += 1
                    if house > right_child and (house - 0) / min_distance <= 1:
                        right_count += 1
                
                if left_count > m / 2 and right_count > m / 2:
                    max_min_distance = min(max_min_distance, mid)
                else:
                    max_min_distance = min(max_min_distance, mid)
            
            if n == 1:
                results.append(mid)
            else:
                left = mid - 1e-5
                right = mid + 1e-5
        
        results.append(max_min_distance)
    
    for result in results:
        print("{:.1f}".format(result))

if __name__ == "__main__":
    main()