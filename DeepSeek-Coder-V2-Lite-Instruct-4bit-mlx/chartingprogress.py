def extract_records(log):
    records = []
    for line in log:
        records.append([c for c in line if c == '*'])
    return records

def sort_log(records):
    sorted_records = []
    for record in records:
        if record:
            min_index = 0
            for i in range(1, len(record)):
                if record[i] < record[min_index]:
                    min_index = i
            sorted_records.append((record[min_index], records.index(record), record))
            records[records.index(record)] = []
    return sorted_records

def print_sorted_log(sorted_records):
    for _, original_index, record in sorted_records:
        for i in range(len(original_index)):
            print(''.join(['*' if records[original_index][i] == '*' else '.' for records in sorted_records]), end='')
        print()

def process_logs(log):
    logs = []
    current_log = []
    for line in log:
        if line == '\n':
            logs.append(current_log)
            current_log = []
        else:
            current_log.append(line)
    logs.append(current_log)
    
    for log in logs:
        records = extract_records(log)
        sorted_records = sort_log(records)
        print_sorted_log(sorted_records)
        print()

# Read input from stdin
import sys
log = []
for line in sys.stdin:
    log.append(line)
process_logs(log)