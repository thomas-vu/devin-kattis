# Python solution to the ICPC matching problem

import sys

def main():
    icpc_records = []
    outside_records = []
    
    # Read ICPC records
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        first_name, last_name, email = line.split()
        icpc_records.append((email.lower(), last_name.lower(), first_name.lower()))
    
    # Read outside records
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        first_name, last_name, email = line.split()
        outside_records.append((email.lower(), last_name.lower(), first_name.lower()))
    
    # Sort records for easy comparison
    icpc_records.sort()
    outside_records.sort()
    
    # Find mismatches
    icpc_mismatches = []
    outside_mismatches = []
    
    i, j = 0, 0
    while i < len(icpc_records) and j < len(outside_records):
        if icpc_records[i] == outside_records[j]:
            i += 1
            j += 1
        elif icpc_records[i] < outside_records[j]:
            icpc_mismatches.append(f"I {icpc_records[i][0]} {icpc_records[i][1].capitalize()} {icpc_records[i][2].capitalize()}")
            i += 1
        else:
            outside_mismatches.append(f"O {outside_records[j][0]} {outside_records[j][1].capitalize()} {outside_records[j][2].capitalize()}")
            j += 1
    
    while i < len(icpc_records):
        icpc_mismatches.append(f"I {icpc_records[i][0]} {icpc_records[i][1].capitalize()} {icpc_records[i][2].capitalize()}")
        i += 1
    
    while j < len(outside_records):
        outside_mismatches.append(f"O {outside_records[j][0]} {outside_records[j][1].capitalize()} {outside_records[j][2].capitalize()}")
        j += 1
    
    # Output results
    if not icpc_mismatches and not outside_mismatches:
        print("No mismatches.")
    else:
        for mismatch in icpc_mismatches:
            print(mismatch)
        for mismatch in outside_mismatches:
            print(mismatch)

if __name__ == "__main__":
    main()