def numerically_distanced_sum(num1, num2):
    # Convert the lists of digits to integers
    int_num1 = int(''.join(map(str, num1)))
    int_num2 = int(''.join(map(str, num2)))
    
    # Calculate the sum of the two numerically distanced numbers
    result = int_num1 + int_num2
    
    # Convert the sum back to a list of digits
    result_digits = [int(digit) for digit in str(result)]
    
    return result_digits

def main():
    t = int(input())  # Number of test cases
    
    for _ in range(t):
        num1 = list(map(int, input().split()))  # First numerically distanced number
        num2 = list(map(int, input().split()))  # Second numerically distanced number
        
        result_digits = numerically_distanced_sum(num1, num2)
        
        # Output the result for each test case
        print(' '.join(map(str, result_digits)))

if __name__ == "__main__":
    main()