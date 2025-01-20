def can_stack(bottom, top, x, y):
    return x * bottom[0] <= top[0] and top[0] <= y * bottom[0] and x * bottom[1] <= top[1] and top[1] <= y * bottom[1]

def main():
    n, x_prime, y_prime = map(int, input().split())
    x = x_prime / 10**6
    y = y_prime / 10**6
    blocks = [list(map(int, input().split())) for _ in range(n)]
    
    # dp[i] will store the maximum height of a tower using the first i blocks
    dp = [1] * n  # Each block can be a tower of height 1 by itself
    
    for i in range(n):
        for j in range(i):
            if can_stack(blocks[j], blocks[i], x, y):
                dp[i] = max(dp[i], dp[j] + 1)
    
    print(max(dp))

if __name__ == "__main__":
    main()