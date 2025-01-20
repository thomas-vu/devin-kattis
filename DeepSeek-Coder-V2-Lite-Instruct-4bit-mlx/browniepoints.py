def calculate_scores(brownie_points):
    stan_score = 0
    ollie_score = 0
    
    for x, y in brownie_points:
        if (x > 0 and y > 0):
            stan_score += 1
        elif (x < 0 and y < 0):
            stan_score += 1
        elif (x < 0 and y > 0):
            ollie_score += 1
        elif (x > 0 and y < 0):
            ollie_score += 1
    
    return stan_score, ollie_score

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        brownie_points = []
        for _ in range(n):
            x, y = map(int, input().split())
            brownie_points.append((x, y))
        
        stan_score, ollie_score = calculate_scores(brownie_points)
        print(stan_score, ollie_score)

if __name__ == "__main__":
    main()