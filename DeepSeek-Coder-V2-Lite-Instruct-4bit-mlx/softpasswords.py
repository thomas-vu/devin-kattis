def should_accept_password(S, P):
    # Check if the passwords are identical
    if S == P:
        return "Yes"
    
    # Check if P can be formed from S by prepending a digit
    for i in range(10):
        if str(i) + S == P:
            return "Yes"
    
    # Check if P can be formed from S by appending a digit
    for i in range(10):
        if S + str(i) == P:
            return "Yes"
    
    # Check if reversing the case of all letters in S makes it equal to P
    reversed_case_S = ''.join([c.lower() if c.isupper() else c.upper() for c in S])
    if reversed_case_S == P:
        return "Yes"
    
    # If none of the conditions are met, reject the password
    return "No"

# Read input
S = input().strip()
P = input().strip()

# Output the result
print(should_accept_password(S, P))