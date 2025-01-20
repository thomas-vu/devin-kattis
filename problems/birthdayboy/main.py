def parse_date(s):
    return tuple(map(int, s.split('-')))

def is_later_date(d1, d2):
    return d1 > d2 if d1[0] == d2[0] else d1[0] > d2[0]

def find_fake_birthday(colleagues):
    current_date = (10, 27)
    longest_interval = -1
    best_date = (10, 28)
    
    for colleague in colleagues:
        name, date_str = colleague.split()
        month, day = map(int, date_str.split('-'))
        if (month, day) < current_date:
            continue
        
        interval = (month - 12) * 30 + day - current_date[1]
        if interval > longest_interval or (interval == longest_interval and is_later_date((month, day), best_date)):
            longest_interval = interval
            best_date = (month, day)
    
    return f"{best_date[0]:02d}-{best_date[1]:02d}"

def main():
    n = int(input())
    colleagues = [input().strip() for _ in range(n)]
    print(find_fake_birthday(colleagues))

if __name__ == "__main__":
    main()