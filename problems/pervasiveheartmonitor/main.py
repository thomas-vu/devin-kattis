def calculate_average_heart_rate(entries):
    heart_rates = []
    current_name = None
    
    for entry in entries:
        words = entry.split()
        if len(words) > 1 and words[-1].replace('.', '', 1).isdigit():
            current_name = ' '.join(words[:-1])
        else:
            heart_rates.extend([float(x) for x in words if '.' in x or ',' in x])
    
    total_heart_rate = sum(heart_rates)
    average_heart_rate = total_heart_rate / len(heart_rates) if heart_rates else 0
    
    return average_heart_rate, current_name

def main():
    entries = []
    
    while True:
        try:
            entry = input()
            entries.append(entry)
        except EOFError:
            break
    
    for entry in entries:
        words = entry.split()
        if len(words) > 1 and words[-1].replace('.', '', 1).isdigit():
            average_heart_rate, name = calculate_average_heart_rate(entries)
            print(f"{average_heart_rate:.2f} {name}")
            entries = [e for e in entries if not e.startswith(name)]
    
if __name__ == "__main__":
    main()