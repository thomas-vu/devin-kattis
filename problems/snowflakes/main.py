def longest_unique_snowflakes(n, snowflakes):
    unique_set = set()
    max_length = 0
    left = 0
    
    for right in range(n):
        while snowflakes[right] in unique_set:
            unique_set.remove(snowflakes[left])
            left += 1
        unique_set.add(snowflakes[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        snowflakes = [int(input()) for _ in range(n)]
        result = longest_unique_snowflakes(n, snowflakes)
        print(result)

if __name__ == "__main__":
    main()