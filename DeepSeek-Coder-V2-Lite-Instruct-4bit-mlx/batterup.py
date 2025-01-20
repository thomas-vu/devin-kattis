n = int(input())
at_bats = list(map(int, input().split()))
total_bases = sum([base for base in at_bats if base > 0])
number_of_official_at_bats = sum([1 for base in at_bats if base > 0])
slugging_percentage = total_bases / number_of_official_at_bats if number_of_official_at_bats > 0 else 0
print("{:.15f}".format(slugging_percentage))