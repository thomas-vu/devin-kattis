def calculate_efficiency_gap(P, D, precincts):
    districts = {}
    for i in range(1, D + 1):
        districts[i] = {"A": 0, "B": 0}
    
    for i in range(P):
        district, a_votes, b_votes = precincts[i]
        districts[district]["A"] += a_votes
        districts[district]["B"] += b_votes
    
    total_wasted_A = 0
    total_wasted_B = 0
    
    for district in districts:
        votes_A = districts[district]["A"]
        votes_B = districts[district]["B"]
        total_votes = votes_A + votes_B
        
        if votes_A > votes_B:
            winner = "A"
            wasted_A = votes_A - ((total_votes // 2) + 1)
            wasted_B = votes_B
        else:
            winner = "B"
            wasted_A = votes_A
            wasted_B = votes_B - ((total_votes // 2) + 1)
        
        total_wasted_A += wasted_A
        total_wasted_B += wasted_B
    
    efficiency_gap = abs(total_wasted_A - total_wasted_B) / (P * 2.0)
    return efficiency_gap

def main():
    P, D = map(int, input().split())
    precincts = [list(map(int, input().split())) for _ in range(P)]
    
    efficiency_gap = calculate_efficiency_gap(P, D, precincts)
    print("{:.10f}".format(efficiency_gap))

if __name__ == "__main__":
    main()