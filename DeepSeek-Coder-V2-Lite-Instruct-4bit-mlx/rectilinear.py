import sys
from itertools import combinations

def is_rectilinear(points):
    for (x1, y1), (x2, y2), (x3, y3), (x4, y4) in combinations(points, 4):
        if x1 != x2 != x3 != x4 and y1 != y2 != y3 != y4:
            return True
    return False

def main():
    input_data = sys.stdin.read().splitlines()
    num_cases = int(input_data[0])
    case_index = 1
    
    for _ in range(num_cases):
        n = int(input_data[case_index])
        points = [tuple(map(int, input_data[case_index + i].split())) for i in range(1, n + 1)]
        case_index += n + 1
        
        if is_rectilinear(points):
            print(len(points))
        else:
            print(-1)

if __name__ == "__main__":
    main()