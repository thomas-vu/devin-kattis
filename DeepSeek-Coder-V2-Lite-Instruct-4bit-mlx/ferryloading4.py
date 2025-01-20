def ferry_crossings(l, m, cars):
    left_side = []
    right_side = []
    
    for car in cars:
        length, side = car.split()
        if side == 'left':
            left_side.append(int(length))
        else:
            right_side.append(int(length))
    
    crossings = 0
    current_bank = 'left'
    
    while left_side or right_side:
        if current_bank == 'left':
            loaded_length = 0
            while left_side and loaded_length + left_side[0] <= l * 100:
                loaded_length += left_side.pop(0)
            crossings += 1
            current_bank = 'right'
        else:
            loaded_length = 0
            while right_side and loaded_length + right_side[0] <= l * 100:
                loaded_length += right_side.pop(0)
            crossings += 1
            current_bank = 'left'
    
    return crossings

def main():
    c = int(input())
    results = []
    
    for _ in range(c):
        l, m = map(int, input().split())
        cars = [input() for _ in range(m)]
        results.append(ferry_crossings(l, m, cars))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()