def time_conversion(time_str):
    units = {
        'sekundur': 1,
        'minuta': 60,
        'klukkustund': 3600,
        'dagur': 8 * 5 * 52 * 5,
        'vika': 7 * 8 * 5 * 52,
        'ar': 365 * 8 * 5 * 52
    }
    
    parts = time_str.split()
    amount = int(parts[0])
    unit = parts[1]
    
    return amount * units[unit]

def main():
    task_frequency = input().strip()
    time_to_perform = input().strip()
    time_to_automate = input().strip()
    
    frequency_units = {
        'sinni': 1,
        'vikulega': 7,
        'daglega': 35,
        'arlega': 1825
    }
    
    frequency = frequency_units[task_frequency.split()[2]]
    time_to_perform = time_conversion(time_to_perform)
    time_to_automate = time_conversion(time_to_automate)
    
    total_manual_time = frequency * time_to_perform
    total_automated_time = 5 * 52 * frequency * time_to_automate
    
    if total_automated_time > total_manual_time:
        print("Borgar sig ekki!")
    else:
        saved_time = total_manual_time - total_automated_time
        print(saved_time)

if __name__ == "__main__":
    main()