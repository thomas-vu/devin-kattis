n, d = map(int, input().split())
a = list(map(int, input().split()))
count = 0
mod_dict = {}

for num in a:
    mod = num // d
    if mod not in mod_dict:
        mod_dict[mod] = 0
    count += mod_dict[mod]
    mod_dict[mod] += 1

print(count)