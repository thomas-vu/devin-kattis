import re

def find_smiles(line):
    pattern = r'[:;][-)]|[:;]\('
    matches = re.finditer(pattern, line)
    return [match.start() for match in matches]

# Read input from stdin
line = input().strip()
smiles_addresses = find_smiles(line)

# Output the result
if smiles_addresses:
    print(' '.join(map(str, smiles_addresses)))