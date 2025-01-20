from collections import defaultdict

def main():
    n = int(input())
    domjudge_results = [input().strip() for _ in range(n)]
    kattis_results = [input().strip() for _ in range(n)]
    
    domjudge_count = defaultdict(int)
    kattis_count = defaultdict(int)
    
    for result in domjudge_results:
        domjudge_count[result] += 1
    for result in kattis_results:
        kattis_count[result] += 1
    
    same_results = 0
    for result in domjudge_count:
        if result in kattis_count:
            same_results += min(domjudge_count[result], kattis_count[result])
    
    print(same_results)

if __name__ == "__main__":
    main()