import sys

def contains_problem(line):
    return 'problem' in line.lower()

for line in sys.stdin:
    print("yes" if contains_problem(line) else "no")