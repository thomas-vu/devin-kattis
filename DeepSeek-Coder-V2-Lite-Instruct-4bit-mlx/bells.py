def generate_bell_performance(n):
    if n == 1:
        return [1]
    
    def generate_rows(current, n):
        if len(current) == n:
            return [current]
        
        rows = []
        for next_num in range(1, n + 1):
            if next_num not in current and (not current or abs(current[-1] - next_num) == 1):
                rows.extend(generate_rows(current + [next_num], n))
        return rows
    
    return generate_rows([1], n)

# Example usage:
n = int(input())
for row in generate_bell_performance(n):
    print(*row)