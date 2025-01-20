n = int(input())
a = list(map(int, input().split()))

# Check if the list is already sorted
if all(str(a[i]) <= str(a[i+1]) for i in range(n-1)):
    print("impossible")
else:
    # Find the number to change and its position
    for i in range(n):
        num_str = str(a[i])
        for j in range(len(num_str)):
            if num_str[j] != str(a[i])[-1]:  # Avoid changing the last digit
                new_num = int(num_str[:j] + str(a[i])[-1] + num_str[j+1:])
                if new_num != a[i]:  # Ensure the number is different
                    temp = list(a)
                    temp[i] = new_num
                    if all(str(temp[k]) <= str(temp[k+1]) for k in range(n-1)):
                        print(" ".join(map(str, temp)))
                        break
                else:
                    continue
            if new_num != a[i]:  # Ensure the number is different
                temp = list(a)
                temp[i] = new_num
                if all(str(temp[k]) <= str(temp[k+1]) for k in range(n-1)):
                    print(" ".join(map(str, temp)))
                    break