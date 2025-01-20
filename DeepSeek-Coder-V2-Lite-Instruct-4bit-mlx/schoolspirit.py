def calculate_group_score(scores):
    n = len(scores)
    total_score = sum([score * ((4/5) ** i) for i, score in enumerate(scores)])
    return total_score / 5

def calculate_new_group_score(scores, index):
    new_scores = scores[:index] + scores[index+1:]
    return calculate_group_score(new_scores)

def main():
    n = int(input())
    scores = [int(input()) for _ in range(n)]
    
    current_score = calculate_group_score(scores)
    g_values = [calculate_new_group_score(scores, i) for i in range(n)]
    average_g = sum(g_values) / n
    
    print("{:.1f}".format(current_score))
    print("{:.10f}".format(average_g))

if __name__ == "__main__":
    main()