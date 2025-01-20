def read_input():
    m = int(input())
    teams = [tuple(map(int, input().split())) for _ in range(m)]
    return m, teams

def find_invitees(m, teams):
    stockholm = set()
    london = set()
    
    for team in teams:
        stockholm.add(team[0])
        london.add(team[1])
    
    invitees = set()
    if 1009 in stockholm:
        invitees.add(1009)
    if 1009 in london:
        invitees.add(1009)
    
    if 1009 in stockholm and 1009 not in london:
        invitees.add(next((member for member in london if member != 1009), None))
    elif 1009 in london and 1009 not in stockholm:
        invitees.add(next((member for member in stockholm if member != 1009), None))
    
    return len(invitees), sorted([1009] + list(invitees))

m, teams = read_input()
k, invitees = find_invitees(m, teams)
print(k)
for invitee in invitees:
    print(invitee)