def closest_number(k):
    keyboard = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']
    ]
    
    def get_value(x, y):
        if 0 <= x < 4 and 0 <= y < 3:
            return keyboard[x][y]
        return None
    
    min_diff = float('inf')
    closest_num = 0
    
    for x in range(4):
        for y in range(3):
            num = get_value(x, y)
            if num is not None:
                diff = abs(int(num) - k)
                if diff < min_diff:
                    min_diff = diff
                    closest_num = int(num)
                elif diff == min_diff and int(num) < closest_num:
                    closest_num = int(num)
    
    return closest_num

def main():
    T = int(input())
    results = []
    for _ in range(T):
        k = int(input())
        results.append(closest_number(k))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()