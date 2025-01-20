def should_yield(arrive, leave, other):
    if (arrive == 'South' and leave == 'West') or (arrive == 'West' and leave == 'South'):
        return other in ['East', 'North']
    elif (arrive == 'South' and leave == 'North') or (arrive == 'North' and leave == 'South'):
        return other in ['East', 'West']
    elif (arrive == 'East' and leave == 'South') or (arrive == 'South' and leave == 'East'):
        return other in ['North', 'West']
    elif (arrive == 'East' and leave == 'North') or (arrive == 'North' and leave == 'East'):
        return other in ['South', 'West']
    elif (arrive == 'West' and leave == 'North') or (arrive == 'North' and leave == 'West'):
        return other in ['East', 'South']
    elif (arrive == 'West' and leave == 'East') or (arrive == 'East' and leave == 'West'):
        return other in ['North', 'South']

arrive = input().strip()
leave = input().strip()
other = input().strip()

if should_yield(arrive, leave, other):
    print("Yes")
else:
    print("No")