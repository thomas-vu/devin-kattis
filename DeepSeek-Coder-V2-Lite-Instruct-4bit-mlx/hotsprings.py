def main():
    n = int(input())
    temperatures = list(map(int, input().split()))
    
    # Sort the temperatures and check if they satisfy the condition
    sorted_temps = sorted(temperatures)
    
    # Create a new sequence by alternating between the smallest and largest elements
    left = 0
    right = n - 1
    result = []
    
    for i in range(n):
        if i % 2 == 0:
            result.append(sorted_temps[left])
            left += 1
        else:
            result.append(sorted_temps[right])
            right -= 1
    
    # Check if the sequence satisfies the condition
    for i in range(1, n - 1):
        if not (abs(result[i - 1] - result[i]) <= abs(result[i] - result[i + 1])):
            print("impossible")
            return
    
    # Output the result
    for temp in result:
        print(temp, end=' ')

if __name__ == "__main__":
    main()