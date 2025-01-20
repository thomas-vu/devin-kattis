def h_index(papers):
    papers.sort()
    n = len(papers)
    h_index = 0
    for i in range(n):
        if papers[i] >= n - i:
            h_index = n - i
    return h_index

n = int(input())
citations = [int(input()) for _ in range(n)]
print(h_index(citations))