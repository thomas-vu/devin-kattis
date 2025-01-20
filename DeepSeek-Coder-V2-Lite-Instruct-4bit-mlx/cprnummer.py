def validate_cpr(cpr):
    if len(cpr) != 11 or cpr[6] != '-':
        return "0"
    
    parts = cpr.split('-')
    if len(parts[1]) != 4:
        return "0"
    
    cpr_digits = parts[0] + parts[1]
    if not cpr_digits.isdigit():
        return "0"
    
    weights = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
    weighted_sum = sum(int(cpr_digits[i]) * weights[i] for i in range(10))
    
    if weighted_sum % 11 == 0:
        return "1"
    else:
        return "0"

# Sample Inputs
print(validate_cpr("070761-4285"))  # Expected Output: 1
print(validate_cpr("051002-4321"))  # Expected Output: 0
print(validate_cpr("310111-0469"))  # Expected Output: 1