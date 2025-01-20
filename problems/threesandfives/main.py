def sum_of_multiples(n):
    def sum_divisible_by(x):
        p = (n - 1) // x
        return x * p * (p + 1) // 2
    
    return sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)

n = int(input())
print(sum_of_multiples(n))