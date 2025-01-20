def is_canonical(coin_system):
    for i in range(len(coin_system)):
        for j in range(i + 1, len(coin_system)):
            if coin_system[i] != 1 and coin_system[j] != 1:
                sum_two_largest = coin_system[i] + coin_system[j]
                for k in range(len(coin_system)):
                    if coin_system[k] < sum_two_largest:
                        continue
                    elif coin_system[k] == sum_two_largest:
                        break
                    else:
                        return "non-canonical"
    return "canonical"

# Read input
n = int(input())
coin_system = list(map(int, input().split()))

# Check if the coin system is canonical
result = is_canonical(coin_system)
print(result)