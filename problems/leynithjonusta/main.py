def extract_email(email):
    parts = email.split('@')
    if len(parts) != 2:
        return None
    local_part = parts[0]
    domain_parts = parts[1].split('.')
    if len(domain_parts) < 2:
        return None
    domain = '.'.join(domain_parts)
    cleaned_email = local_part.replace(' ', '') + '@' + domain
    return cleaned_email

# Read input from stdin
email = input().strip()

# Process the email address and print the result
cleaned_email = extract_email(email)
if cleaned_email:
    print(cleaned_email)