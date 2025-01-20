def can_pay_mortgage(X, Y, N, r):
    # Convert annual interest rate to monthly
    monthly_interest_rate = (r / 100) / 12
    
    # Calculate the total number of months in N years
    total_months = N * 12
    
    # Initialize the current debt with the principal amount
    current_debt = X
    
    # Iterate over each month to check if the alien can pay the mortgage
    for _ in range(total_months):
        # Calculate interest for the month and add it to the current debt
        interest = current_debt * monthly_interest_rate
        current_debt += interest
        
        # Subtract the monthly payment from the current debt
        current_debt -= Y
        
        # If the remaining debt is less than or equal to zero, the alien can pay the mortgage
        if current_debt <= 0:
            return "YES"
    
    # If the alien cannot pay off the debt within N years, return "NO"
    return "NO"

# Read input until EOF
while True:
    X, Y, N, r = map(float, input().split())
    if X == 0 and Y == 0 and N == 0 and r == 0:
        break
    result = can_pay_mortgage(int(X), int(Y), int(N), r)
    print(result)