def min_changes_to_balance(mobile):
    def evaluate(expr):
        if isinstance(expr, int):
            return expr
        left_weight, right_weight = evaluate(expr[0]), evaluate(expr[1])
        return left_weight + right_weight

    def torque(expr, target):
        if isinstance(expr, int):
            return abs(expr - target)
        left_weight, right_weight = evaluate(expr[0]), evaluate(expr[1])
        left_torque = torque(expr[0], target)
        right_torque = torque(expr[1], target)
        return left_torque + right_torque

    def find_min_changes(expr, target):
        if isinstance(expr, int):
            return int(expr != target)
        left_weight = evaluate(expr[0])
        right_weight = evaluate(expr[1])
        left_changes = find_min_changes(expr[0], target)
        right_changes = find_min_changes(expr[1], target)
        return min(left_changes + right_changes, left_weight != target, right_weight != target)

    root_weight = evaluate(mobile)
    return find_min_changes(mobile, root_weight // 2)

# Read number of test cases
num_test_cases = int(input())
results = []
for _ in range(num_test_cases):
    mobile = eval(input())
    results.append(min_changes_to_balance(mobile))

for result in results:
    print(result)