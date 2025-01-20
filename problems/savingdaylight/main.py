def time_diff(rise, set):
    rise_hour, rise_minute = map(int, rise.split(':'))
    set_hour, set_minute = map(int, set.split(':'))
    total_minutes = (set_hour * 60 + set_minute) - (rise_hour * 60 + rise_minute)
    return total_minutes // 60, total_minutes % 60

def main():
    while True:
        try:
            line = input()
            if not line:
                break
            month, day, year, rise_time, set_time = line.split()
            hours, minutes = time_diff(rise_time, set_time)
            print(f"{month} {day} {year} {hours} hours {minutes} minutes")
        except EOFError:
            break

if __name__ == "__main__":
    main()