def calculate_salary(pension_fund, supplementary_fund, salaries):
    total_salary = sum(salaries)
    pension_fee = int(total_salary * (pension_fund / 100))
    supplementary_fee = int(total_salary * (supplementary_fund / 100))
    tax_base = total_salary - pension_fee - supplementary_fee
    
    # Calculate income tax
    if tax_base <= 409986:
        income_tax = int(tax_base * 0.3145)
    elif tax_base <= 1151012:
        income_tax = int(409986 * 0.3145 + (tax_base - 409986) * 0.3795)
    else:
        income_tax = int(409986 * 0.3145 + (1151012 - 409986) * 0.3795 + (tax_base - 1151012) * 0.4625)
    
    # Calculate communal tax
    communal_tax = int(tax_base * 0.1467)
    
    # Calculate withholding tax
    withholding_tax = income_tax + communal_tax
    
    # Calculate personal tax exemption
    personal_tax_exemption = 59665
    
    if withholding_tax <= personal_tax_exemption:
        remaining_exemption = personal_tax_exemption - withholding_tax
        final_salary = total_salary - remaining_exemption
    else:
        final_salary = total_salary - withholding_tax
    
    return int(final_salary)

# Read input
pension_fund = float(input().strip())
supplementary_fund = float(input().strip())
salaries = [float(input().strip()) for _ in range(12)]

# Calculate the result
result = calculate_salary(pension_fund, supplementary_fund, salaries)
print(result)