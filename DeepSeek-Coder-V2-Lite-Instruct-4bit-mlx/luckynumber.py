import math

def count_lucky_numbers(n):
    # Function to check if the number is lucky
    def is_lucky(num_str, k):
        return int(num_str[:k]) % k == 0
    
    # Generate all possible lucky numbers with n digits
    def generate_lucky_numbers(num_str, k):
        if k == len(num_str):
            return [num_str]
        result = []
        for next_digit in range(10):
            if is_lucky(num_str + str(next_digit), k):
                result.extend(generate_lucky_numbers(num_str + str(next_digit), k + 1))
        return result
    
    # Generate all lucky numbers with n digits
    lucky_numbers = generate_lucky_numbers("", 1)
    
    # Return the count of lucky numbers with n digits
    return len(lucky_numbers)

# Main function to calculate the supply for n-digit lucky numbers
def main():
    n = int(input())
    supply = count_lucky_numbers(n)
    print(supply)

if __name__ == "__main__":
    main()