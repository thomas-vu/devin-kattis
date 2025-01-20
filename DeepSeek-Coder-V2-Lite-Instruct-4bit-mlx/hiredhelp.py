def max_employees(N, K, deadlines):
    # Sort the shoes by their deadlines in ascending order
    sorted_deadlines = sorted(range(N), key=lambda i: deadlines[i])
    
    # Initialize the number of employees and a list to track assigned shoes
    num_employees = 0
    assigned_shoes = [False] * N
    
    # Assign shoes to employees based on the sorted deadlines
    for i in range(N):
        if not assigned_shoes[sorted_deadlines[i]]:
            # Assign K shoes to the employee if possible
            for j in range(K):
                if sorted_deadlines[i] + j < N and not assigned_shoes[sorted_deadlines[i] + j]:
                    assigned_shoes[sorted_deadlines[i] + j] = True
                else:
                    break
            num_employees += 1
        if all(assigned_shoes):
            break
    
    return num_employees

# Read input
N, K = map(int, input().split())
deadlines = list(map(int, input().split()))

# Calculate and print the result
print(max_employees(N, K, deadlines))