n = int(input())
views_dict = {}
for _ in range(n):
    s, a = input().split()
    a = int(a)
    if s in views_dict:
        views_dict[s] += a
    else:
        views_dict[s] = a
most_popular = max(views_dict, key=views_dict.get)
print(most_popular)