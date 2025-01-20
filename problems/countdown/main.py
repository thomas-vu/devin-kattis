from itertools import permutations, product

def evaluate_expression(nums, ops):
    stack = []
    for num in nums:
        if isinstance(num, int):
            stack.append(num)
        else:
            b = stack.pop()
            a = stack.pop()
            if num == '+':
                stack.append(a + b)
            elif num == '-':
                stack.append(a - b)
            elif num == '*':
                stack.append(a * b)
            elif num == '/':
                if a % b == 0:
                    stack.append(a // b)
                else:
                    return float('inf')  # Invalid division, avoid fractions
    return stack[0] if stack else float('inf')

def generate_expressions(nums):
    operators = ['+', '-', '*', '/']
    operator_combinations = product(operators, repeat=len(nums) - 1)
    valid_expressions = set()
    
    for ops in operator_combinations:
        for perm in permutations(nums):
            try:
                result = evaluate_expression(perm, ops)
                if result != float('inf'):
                    valid_expressions.add(result)
            except:
                pass
    return valid_expressions

def main():
    C = int(input())
    results = []
    
    for _ in range(C):
        nums = list(map(int, input().split()))
        T = int(input())
        
        valid_nums = generate_expressions(nums)
        closest_value = min(valid_nums, key=lambda x: abs(x - T))
        
        results.append((T, closest_value))
    
    for target, best_approx in results:
        print(f"Target: {target}")
        print(f"Best approx: {best_approx}")
        print()

if __name__ == "__main__":
    main()