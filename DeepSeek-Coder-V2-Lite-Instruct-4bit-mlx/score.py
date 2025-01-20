def parse_time(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

def format_time(seconds):
    minutes = seconds // 60
    seconds %= 60
    return f"{minutes}:{seconds:02d}" if minutes < 10 else f"{minutes}:{seconds:02d}"

n = int(input())
home_lead = 0
away_lead = 0
home_time = 0
away_time = 0
last_time = 0
home_score = 0
away_score = 0
for _ in range(n):
    team, points, time_str = input().split()
    points = int(points)
    minutes, seconds = map(int, time_str.split(':'))
    current_time = minutes * 60 + seconds
    
    if team == 'H':
        home_score += points
    else:
        away_score += points
    
    if home_score > away_score:
        if home_lead < (current_time - last_time):
            home_lead = current_time - last_time
    elif away_score > home_score:
        if away_lead < (current_time - last_time):
            away_lead = current_time - last_time
    
    last_time = current_time

if home_score > away_score:
    winner = 'H'
elif away_score > home_score:
    winner = 'A'
else:
    winner = 'H' if home_score > away_score else 'A'

total_time = 32 * 60 - (last_time if home_score != away_score else 0)
home_lead = format_time(max(home_lead, total_time - home_lead))
away_lead = format_time(max(away_lead, total_time - away_lead))

print(winner)
print(home_lead)
print(away_lead)