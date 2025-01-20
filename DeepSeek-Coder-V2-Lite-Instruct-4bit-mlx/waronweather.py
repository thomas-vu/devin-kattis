import math

def is_in_line_of_sight(satellite, target):
    distance = math.sqrt((satellite[0] - target[0])**2 + (satellite[1] - target[1])**2 + (satellite[2] - target[2])**2)
    return distance <= 150 + target[3]

def main():
    while True:
        k, m = map(int, input().split())
        if k == 0 and m == 0:
            break
        
        satellites = [list(map(float, input().split())) for _ in range(k)]
        targets = [list(map(float, input().split())) for _ in range(m)]
        
        targets_hit = 0
        for target in targets:
            can_hit = False
            for satellite in satellites:
                if is_in_line_of_sight(satellite, target):
                    can_hit = True
                    break
            if can_hit:
                targets_hit += 1
        
        print(targets_hit)

if __name__ == "__main__":
    main()